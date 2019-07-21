# -*- coding: utf-8 -*-
import scrapy

import re
import json

from ichunqiu import items


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['www.ichunqiu.com']
    # start_urls = ['https://www.ichunqiu.com/courses']

    url = "https://www.ichunqiu.com/courses/ajaxCourses"

    # 空串 -- 全部    1 -- 收费        2 -- 免费
    mode = 2
    cur_page = 1
    max_page = 11

    def start_requests(self):
        formdata = {
            'courseTag': '',
            'courseDiffcuty': '',
            'IsExp': '',
            'producerId': '',
            'orderField': '',
            'orderDirection': '',
            'pageIndex' : str(self.cur_page),
            'tagType': '',
            'isOpen': str(self.mode)
        }
        yield scrapy.FormRequest(url = self.url, formdata = formdata, callback = self.parse)

    def parse(self, response):
        datas = json.loads(response.body_as_unicode())

        if datas['course']['result']:
            for data in datas['course']['result']:
                name = data['courseName']
                price = data['presentPrice']
                views = data['buyNum']
                date = data['createTime']
                print(items.IchunqiuItem(name = name, price = price, views = views, date = date))
                yield items.IchunqiuItem(name = name, price = price, views = views, date = date)


        if self.cur_page < self.max_page:
            self.cur_page = self.cur_page + 1
            formdata = {
                'pageIndex': str(self.cur_page),
                'isOpen': str(self.mode)
            }
            yield scrapy.FormRequest(url = self.url, formdata = formdata, callback = self.parse)