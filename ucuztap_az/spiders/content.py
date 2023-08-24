import scrapy


class ContentSpider(scrapy.Spider):
    name = "content"
    allowed_domains = ["ucuztap.az"]
    start_urls = ["https://ucuztap.az/elan/6769693-sat%C4%B1s-heyet-evi/"]

    def parse(self, response):
        yield {
            'name':response.css('h3.m-t-1::text').get(),
            'phone':response.css('strong.fs-20::text').getall()
        }
