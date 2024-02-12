import scrapy


class Spider36Spider(scrapy.Spider):
    name = "spider36"
   
    start_urls = ["https://boardgamegeek.com/boardgame/161936/pandemic-legacy-season-1"]

    def parse(self, response):
        # Estrai e stampa le meta tag della pagina
        meta_tags = response.xpath('//meta')
        for tag in meta_tags:
            name = tag.xpath('@name').get()
            content = tag.xpath('@content').get()
            yield {
                'name': name,
                'content': content
            }
        