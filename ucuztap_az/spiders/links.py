import scrapy


class LinksSpider(scrapy.Spider):
    name = "links"
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
        # Extract links from the current page
        for link in response.css('.thumbnail.i-product a[href]::attr(href)').getall():
            yield {
                'links': link
            }

        # Follow pagination links
        next_page_relative = response.css('.pagination li.active + li a::attr(href)').get()
        if next_page_relative:
            next_page_absolute = response.urljoin(next_page_relative)
            yield scrapy.Request(url=next_page_absolute, callback=self.parse)
