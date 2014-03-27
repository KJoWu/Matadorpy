from scrapy.spider import Spider
from scrapy.selector import Selector
from urlscraper.items import ProteinInfo


class MatadorSpider(Spider):
    name = "matador"
    allowed_domains = ["http://matador.embl.de/proteins/"]
    start_urls = [
        "http://matador.embl.de/proteins/"
    ]
    base = "http://matador.embl.de/proteins/"

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul/li')
        items=[]
        for site in sites:
            item=ProteinInfo()
            item['proteinName'] =site.xpath('a/text()').extract
            item['url'] = base + site.xpath('a/@href').extract()
            items.append(item)
        return items


