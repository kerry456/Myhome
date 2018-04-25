# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WoaiwojiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    area = scrapy.Field()
    price = scrapy.Field()
    rent_method = scrapy.Field()
    address = scrapy.Field()
    url = scrapy.Field()

class Woaiwojia_detail_Item(scrapy.Item):
    title = scrapy.Field()
    rent = scrapy.Field()
    floor = scrapy.Field()
    house_type = scrapy.Field()
    area = scrapy.Field()
    payment_method = scrapy.Field()
    build_year = scrapy.Field()
    rent_method = scrapy.Field()
    subway = scrapy.Field()
    contact = scrapy.Field()
    telephone_number = scrapy.Field()
