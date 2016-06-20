# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChaoshiCategoryItem(scrapy.Item):
    # define the fields for your item here like:
    cateUrl = scrapy.Field()  # 分类的url
    cateName = scrapy.Field()  # 分类名称 存储二级分类


class ChaoshiGoodsItem(scrapy.Item):
    # define the fields for your item here like:
    goodsName = scrapy.Field()
    goodsId = scrapy.Field()
    goodsUrl = scrapy.Field()
    goodsPrice = scrapy.Field()
    goodsPicUrl = scrapy.Field()
