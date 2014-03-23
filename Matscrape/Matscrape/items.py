from scrapy.item import Item, Field

class DrugInfo(Item):
   drugname =Field()
   link= Field()
   full_name=Field()
   interaction1= Field()
   interaction2=Field()
   interaction3=Field()
   
