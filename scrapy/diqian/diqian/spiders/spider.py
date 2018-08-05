# -*- coding: utf-8 -*-
import scrapy
from diqian.items import DiqianItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['www.qidian.com']
    start_urls = ['https://www.qidian.com/free/all?orderId=&vip=hidden&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=1&page='+str(N) for N in range(1,1000)]    #47374

    def parse(self, response):
        novel_list = response.xpath("//div[@class='book-img-text']/ul/li")
        for i_item in novel_list:
            novel_item = DiqianItem()
            novel_item['name'] = i_item.xpath("./div[@class='book-mid-info']//a/text()").extract_first()
            novel_item['author'] = i_item.xpath("./div[@class='book-mid-info']/p/a[@class='name']/text()").extract_first()
            novel_item['status'] = i_item.xpath("./div[@class='book-mid-info']/p[1]/span[1]/text()").extract_first()
            novel_item['intro'] = i_item.xpath("./div[@class='book-mid-info']/p[2]/text()").extract_first().strip()
            novel_item['tage'] = i_item.xpath("./div[@class='book-mid-info']/p[1]/a[2]/text()").extract_first()
            novel_item['sub_tage'] = i_item.xpath("./div[@class='book-mid-info']/p[1]/a[3]/text()").extract_first()
            yield novel_item

        next_link = response.xpath("//div[@class='lbf-pagination']/ul/li[9]/a/@href").extract_first()
        if next_link is not None:
            yield scrapy.Request("https:"+str(next_link), callback=self.parse)
