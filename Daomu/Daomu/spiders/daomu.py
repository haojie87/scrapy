# -*- coding: utf-8 -*-
''' 标题 + 标题 + 内容'''
import scrapy
from ..items import DaomuItem


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    # 一级页面
    def parse(self, response):
        a_list = response.xpath('//li[contains(@id,"menu-item-20")]/a')
        for a in a_list:
            item = DaomuItem()
            # item['title']:盗墓笔记一 - 七星鲁王宫
            item['title'] = a.xpath('./text()').get()
            link = a.xpath('./@href').get()
            # 把link交给调度器入队列
            yield scrapy.Request(url=link,
                                 # 在不同的解析函数间传递数据
                                 meta={'item':item},
                                 callback=self.parse_two_html)

    # 解析二级页面
    def parse_two_html(self, response):
        # 获取item
        item = response.meta['item']
        # article_list:[节点对象一,节点对象二]
        article_list = response.xpath('//article')
        for article in article_list:
            # item['name']:'七星鲁王 第一章 血尸'
            name = article.xpath('./a/text()').get()
            two_link = article.xpath('./a/@href').get()
            # 交给调度器
            yield scrapy.Request(url=two_link,meta={'item':item,'name':name},callback=self.parse_three_page)

    # 三级页面
    def parse_three_page(self, response):
        item= response.meta['item']
        item['name'] = response.meta['name']
        # con_list:['段落一','段落二','段落三']
        con_list =response.xpath('//article[@class="article-content"]//p/text()').extract()
        item['content'] = '/n'.join(con_list)

        yield item






