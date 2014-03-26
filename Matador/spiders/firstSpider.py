from scrapy.spider import Spider
from scrapy.selector import Selector
from Matador.items import DrugInfo


class MatadorSpider(Spider):
    name = "matador"
    allowed_domains = ["http://matador.embl.de/drugs/"]
    start_urls = [
        "http://matador.embl.de/drugs/"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul/li')
        items=[]
        for site in sites:
            item=DrugInfo()
            item['link'] = site.xpath('a/@href').extract()
            item['drugname'] =site.xpath('a/text()').extract()
            items.append(item)
        return items