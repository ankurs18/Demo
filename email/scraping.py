import scrapy

class imdbscraping(scrapy.Spider):
    name = 'imdb_spider'
    start_urls = ['http://www.epguides.com/BetterCallSaul/']
    def parse(self, response):
        #SET_SELECTOR = '.set'
        for brickset in response.xpath("//div[@id='eplist']"):
            
            yield {
                'name': brickset.xpath('pre').extract_first()
            }
            
scraper = imdbscraping()

scraper.start_requests()