# -*- coding: utf-8 -*-
import scrapy
from sina_kaoshi import items


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['kaoshi.edu.sina.com.cn']
    start_urls = ['http://kaoshi.edu.sina.com.cn/college/scorelist?tab=file&wl=2&local=11&syear=2019&page=1']

    def parse(self, response):
        results = response.xpath('//div[@class="tabsContainer"]/table[@class="tbL2"]//tr[@class!="tbL2title"]')
        for result in results:
            year = result.xpath('./td[1]/text()').extract_first()
            location = result.xpath('./td[2]/text()').extract_first()
            category = result.xpath('./td[3]/text()').extract_first()
            score = result.xpath('./td[4]/text()').extract_first()
            number = result.xpath('./td[5]/text()').extract_first()
            total_number = result.xpath('./td[6]/text()').extract_first()
            item = items.SinaKaoshiItem(year = year, location = location, category = category, score = score, number = number, total_number = total_number)
            # TODO
            # delete print
            print(item)
            yield item

        now_page_number = response.xpath('//div[@class="pageNumWrap"]/@page').extract_first()
        total_page_number = response.xpath('//div[@class="pageNumWrap"]/@totalpage').extract_first()
        if ((int(now_page_number) + 1) <= int(total_page_number)):
            yield scrapy.Request("http://kaoshi.edu.sina.com.cn/college/scorelist?tab=file&wl=2&local=11&syear=2019&page=" + str(int(now_page_number) + 1), callback = self.parse)