import scrapy

class HackernewsScraperItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()

