from scrapy.spider import Spider
from scrapy.selector import Selector
from IntScraper.items import ScraperInfo


class MatadorSpider(Spider):
    name = "matSpider"
    allowed_domains = ["http://matador.embl.de/proteins/"]

    #Paste all the URLS here
    start_urls = [
        "http://matador.embl.de/proteins/D015105/"
    ]

    def parse(self, response):
        sel = Selector(response)
        items=[]
        item=ScraperInfo()
        item['Name'] = sel.xpath("//h1").extract()
        item['Direct'] = sel.xpath("//ul//li[contains(.,'Direct interaction')]/ul//li/a").extract()
        item['Indirect'] = sel.xpath("//ul//li[contains(.,'Indirect interaction')]/ul//li/a").extract()
        return items
        
        


      

