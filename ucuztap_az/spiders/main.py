import scrapy

class CombinedSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["ucuztap.az"]

    start_urls = [
        "https://ucuztap.az/sexsi-esyalar/?page=1",
        "https://ucuztap.az/ev-ve-bag-ucun/?page=1",
        "https://ucuztap.az/elektronika/?page=1",
        "https://ucuztap.az/hobbi-ve-asude/?page=1",
        "https://ucuztap.az/neqliyyat/?page=1",
        "https://ucuztap.az/dasinmaz-emlak/?page=1",
        "https://ucuztap.az/is-ve-biznes/?page=1"
    ]

    def parse(self, response):
        # Extract links from the search page
        for link in response.css('.thumbnail.i-product a[href]::attr(href)').getall():
            yield response.follow(link, callback=self.parse_content)

        # Follow pagination links
        next_page_relative = response.css('.pagination li.active + li a::attr(href)').get()
        if next_page_relative:
            next_page_absolute = response.urljoin(next_page_relative)
            yield scrapy.Request(url=next_page_absolute, callback=self.parse)

    def parse_content(self, response):
        # Extract content details from the individual item pages
        yield {
            'link': response.url,
            'name': response.css('h3.m-t-1::text').get(),
            'phone': response.css('strong.fs-20::text').getall(),
        }
