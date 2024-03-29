# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    # 最终需要的数据:{'name':'','star':'','time':''}
    # 名称 + 主演 + 上映时间
    name = scrapy.Field()
    star = scrapy.Field()
    time = scrapy.Field()
