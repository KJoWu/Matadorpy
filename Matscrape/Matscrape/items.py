from scrapy.item import Item, Field

class DrugInfo(Item):
   drugname =Field()
   link= Field()
   
