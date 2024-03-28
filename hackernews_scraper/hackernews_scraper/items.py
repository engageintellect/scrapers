import scrapy

class HackernewsScraperItem(scrapy.Item):
    # define the fields for your item here
    title = scrapy.Field()
    url = scrapy.Field()

