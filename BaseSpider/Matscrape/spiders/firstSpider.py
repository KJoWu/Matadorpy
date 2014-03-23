from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from Matscrape.items import DrugInfo
import re

class MatadorSpider(CrawlSpider):
    name = "matador"
    allowed_domains = ["http://matador.embl.de/drugs/"]
    start_urls = ["http://matador.embl.de/drugs/"]
    rules = ( Rule(SgmlLinkExtractor(allow=(r'\d{4}\/', )), callback='parse_item',follow=True),
    )
    
    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul/li')
        items=[]
        for site in sites:
            item=DrugInfo()
            item['drugname'] =site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()

    def parse_item(self, response):
        print "ASAAAAAAAAAAAAAAAAAAAAAAA"

        self.log('Hi, this is an item page! %s' % response.url)

        sel = Selector(response)
        yo = sel.xpath('//ul/li/a/@href').extract()
        return item

