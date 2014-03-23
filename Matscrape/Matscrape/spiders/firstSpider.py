from scrapy.spider import Spider
from scrapy.selector import Selector


class MatadorSpider(Spider):
    name = "matador"
    allowed_domains = ["http://matador.embl.de/drugs/"]
    start_urls = [
        "http://matador.embl.de/drugs/"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul/li')
        for site in sites:
            #link = site.xpath('a/@href').extract()  
            drugname =site.xpath('a/text()').extract()
            print "drug is", drugname
