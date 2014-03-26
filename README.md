##Matador Scripts

Author: Kim Wu

2 very simple scripts for extracting info from Matador. 

###Matador Spider:
#####Run in the command line:   
#####scrapy crawl matador -o items.csv -t csv

Will compile a csv of all names and url of drugs. 


Notes: Technically this could have been done with a CrawlSpider, but it would have slighlty overcomplicated the issue. Hence, 2 base spiders were used. 

###Interactions Scraper:
#####run something  

Will go through all urls on the site and gather information about direct/indirect interaction and pubmed id's. 



