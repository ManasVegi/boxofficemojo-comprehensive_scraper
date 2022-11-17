# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    titleId = scrapy.Field()
    directors = scrapy.Field()
    writers = scrapy.Field()
    producers = scrapy.Field()
    composers = scrapy.Field()
    editors = scrapy.Field()
    actor1 = scrapy.Field()
    actor2 = scrapy.Field()
    actor3 = scrapy.Field()
