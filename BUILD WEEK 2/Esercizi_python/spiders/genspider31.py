import scrapy


class Genspider31Spider(scrapy.Spider):
    name = "genspider31"
    allowed_domains = ["towardsdatascience.com"]
    start_urls = ["https://towardsdatascience.com/whats-new-in-pandas-2-2-e3afe6f341f5"]

    def parse(self, response):
        titles = response.css('h1::text').getall()
        for title in titles:
            yield {'title': title}
        
