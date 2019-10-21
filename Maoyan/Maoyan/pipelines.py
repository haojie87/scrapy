# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(item['name'],item['star'],item['time'])
        return item

# 存入MySQL数据库的管道
import pymysql
from .settings import *


class MaoyanMysqlPipeline(object):
    def open_spider(self,spider):
        # 爬虫项目启动时执行一次,一般用于数据库连接
        self.db = pymysql.connect(host=MYSQL_HOST,user=MYSQL_USER,password=MYSQL_PWD,database=MESQL_DB,charset=MYSQL_CHARSET)
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        # 把数据存入到数据库

        return item

    def close_spider(self,spider):
        #爬虫项目结束时只执行一次
        self.cursor.close()
        self.db.close()

# 流程
# 1.settings.py 中定义变量
# 2.pipelines.py中写存入数据库代码
# 3.setting.py中开启对应管道
#
# MONGO_HOST= 'localhost'
# MONGO_PORT =27017

