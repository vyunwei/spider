# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from urllib import request


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        name = item['name']
        lt = item['linkLT']
        dx = item['linkDX']
        print(lt)
        # print(name)
        try:
            request.urlretrieve(lt, 'D:\\song\\%s.mp3' % (name))

        except:
            request.urlretrieve(dx, 'D:\\song\\%s.mp3' % (name))
        else:
            print("无法下载")
        return item
