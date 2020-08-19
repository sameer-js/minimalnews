# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MinimalnewsItem(scrapy.Item):
    # define the fields for your item here like:
    headline = scrapy.Field()
    link = scrapy.Field()
