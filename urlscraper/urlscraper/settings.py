# Scrapy settings for urlscraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'urlscraper'

SPIDER_MODULES = ['urlscraper.spiders']
NEWSPIDER_MODULE = 'urlscraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'urlscraper (+http://www.yourdomain.com)'
