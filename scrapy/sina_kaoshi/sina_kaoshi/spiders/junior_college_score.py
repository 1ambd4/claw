# -*- coding: utf-8 -*-
import scrapy
from sina_kaoshi import items


class JuniorCollegeScoreSpider(scrapy.Spider):
    name = 'junior_college_score'
    allowed_domains = ['kaoshi.edu.sina.com.cn']
    start_urls = ['http://kaoshi.edu.sina.com.cn/college/scorelist?tab=&wl=2&local=11&provid=11&batch=21&syear=2018&page=1']

    def parse(self, response):
        results = response.xpath('//div[@class="tabsContainer"]//tr[@class="tbl2tbody"]')
        for result in results:
            name = result.xpath('./td[1]/a/text()').extract_first()
            location = result.xpath('./td[2]/text()').extract_first()
            category = result.xpath('./td[3]/text()').extract_first()
            batch = result.xpath('./td[4]/text()').extract_first()
            year = result.xpath('./td[5]/text()').extract_first()
            max_score = result.xpath('./td[6]/text()').extract_first()
            avg_score = result.xpath('./td[7]/text()').extract_first()

            item = items.JuniorCollegeItem(name = name, location = location, category = category, batch = batch, year = year, max_score = max_score, avg_score = avg_score)
            print(item)
            yield item

        now_page_number = response.xpath('//div[@class="pageNumWrap"]/@page').extract_first()
        total_page_number = response.xpath('//div[@class="pageNumWrap"]/@totalpage').extract_first()
        if ((int(now_page_number) + 1) <= int(total_page_number)):
            yield scrapy.Request("http://kaoshi.edu.sina.com.cn/college/scorelist?tab=&wl=2&local=11&provid=11&batch=21&syear=2018&page=" + str(int(now_page_number) + 1), callback=self.parse)