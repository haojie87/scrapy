# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4?offset=']
    offset = 0

    # response 为start_urls中的响应对象
    def parse(self, response):
        # 基准xpath ,匹配电影信息的dd节点对象列表
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        # 给item.py中的类实例化
        item = MaoyanItem()
        for dd in dd_list:
            # 或者item['name'] = dd.xpath('').extract_first()-->老版本只能用此方法
            item['name'] = dd.xpath('./a/@title').get().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()

            yield item

        if self.offset < 90:
            self.offset += 10
        url = 'https://maoyan.com/board/4?offset=' + str(self.offset)
        # 把url交给调度器入队列
        yield scrapy.Request(url=url,callback=self.parse)