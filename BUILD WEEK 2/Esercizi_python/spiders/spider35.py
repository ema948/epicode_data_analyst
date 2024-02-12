import scrapy

class Genspider35Spider(scrapy.Spider):
    name = "spider35"
    allowed_domains = ["towardsdatascience.com"]
    start_urls = ["https://towardsdatascience.com/whats-new-in-pandas-2-2-e3afe6f341f5"]

    def parse(self, response):
        # Extracting titles using XPath
        titles = response.xpath('//h1/text()').getall()
        for title in titles:
            yield {'title': title}

