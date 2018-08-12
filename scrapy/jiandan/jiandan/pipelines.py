# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import os

class JiandanPipeline(object):
    def process_item(self, item, spider):
        path = os.path.abspath('./')
        save_path = path + '/meizi'
        if not os.path.exists(save_path):
            os.mkdir(save_path)
            print('文件夹创建成功！')
        img_url = item['img_url']
        img_name = item['img_name']
        save_img = save_path + '/' + img_name + '.jpg'
        r = requests.get(img_url)

        print('正在下载图片%s......' % img_name)

        with open(save_img, 'wb') as f:
            f.write(r.content)
        f.close()
