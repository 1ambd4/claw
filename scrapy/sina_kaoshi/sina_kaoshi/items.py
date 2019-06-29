# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaKaoshiItem(scrapy.Item):
    year = scrapy.Field()
    location = scrapy.Field()
    category = scrapy.Field()
    score = scrapy.Field()
    number = scrapy.Field()
    total_number = scrapy.Field()

class JuniorCollegeItem(scrapy.Item):
    name = scrapy.Field()
    location = scrapy.Field()
    category = scrapy.Field()
    batch = scrapy.Field()
    year = scrapy.Field()
    max_score = scrapy.Field()
    avg_score = scrapy.Field()