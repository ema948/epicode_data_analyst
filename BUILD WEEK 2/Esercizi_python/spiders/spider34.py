import scrapy


class Spider34Spider(scrapy.Spider):
    name = "spider34"
   
    start_urls = ["https://www.lafeltrinelli.it/libri-inglese/science-computer-technology"]

    def parse(self, response):
        for libri in response.css('div.cc-product-list-item'):
            yield {'title': libri.css('a.cc-title::text').get(),
                   'image link' : libri.css('img').attrib.get('src')
                  }
        
