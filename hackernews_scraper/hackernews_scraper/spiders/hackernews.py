import scrapy
from ..items import HackernewsScraperItem  # Import your item class

class HackernewsSpider(scrapy.Spider):
    name = 'hackernews'
    allowed_domains = ['news.ycombinator.com']
    start_urls = ['http://news.ycombinator.com/']


    def parse(self, response):
        for post in response.css('tr.athing'):
            title = post.css('td.title a::text').get()
            url = post.css('td.title a::attr(href)').get()
            if title and url:  # Check if both title and url are not None
                yield {
                    'title': title,
                    'url': url,
                }


