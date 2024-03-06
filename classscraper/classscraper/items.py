# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ClassscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ClassItem(scrapy.Item):
    major = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    prereq = scrapy.Field()
