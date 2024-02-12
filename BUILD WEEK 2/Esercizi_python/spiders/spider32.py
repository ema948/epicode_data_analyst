import scrapy


class Spider32Spider(scrapy.Spider):
    name = "spider32"
    allowed_domains = ["towardsdatascience.com"]
    start_urls = ["https://towardsdatascience.com/whats-new-in-pandas-2-2-e3afe6f341f5"]

    def parse(self, response):       
        links=response.css('a::attr(href)').getall()
        for data in [{'link':x} for x in links]:
            yield data
