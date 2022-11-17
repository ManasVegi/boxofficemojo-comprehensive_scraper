# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    titleId = scrapy.Field()
    domestic_gross = scrapy.Field()
    worldwide_gross = scrapy.Field()
    domestic_opening = scrapy.Field()
    # theatres = scrapy.Field()
    earliest_release_date = scrapy.Field()
    distributor = scrapy.Field()
    budget = scrapy.Field()
    running_time = scrapy.Field()
    mpaa = scrapy.Field()
    genres = scrapy.Field()
