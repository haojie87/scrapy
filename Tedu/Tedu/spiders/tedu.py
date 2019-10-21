# -*- coding: utf-8 -*-
import scrapy
from ..items import TeduItem


class TeduSpider(scrapy.Spider):
    name = 'tedu'
    allowed_domains = ['http://code.tarena.com.cn/AIDCode/']
    start_urls = ['http://http://code.tarena.com.cn/AIDCode//']

    def parse(self, response):
        item = TeduItem()
        link_list = response.xpath('//pre/a')
        for link in link_list:
            link = link.xpath('./@href').get()
            item['name'] =link

        yield item


