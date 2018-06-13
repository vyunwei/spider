# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem


class YoubanSpider(scrapy.Spider):
    name = 'youban'
    allowed_domains = ['youban.com']
    start_urls = ['http://www.youban.com/mp3-t4419.html']

    def parse(self, response):
        data = response.xpath("//div[@class='Mp3gequlistMain']/ul/li/span")

        for node in data:
            href = node.xpath('./a/@href').extract()
            yield scrapy.Request(href[0], callback=self.info)
    def info(self, response):
        href = response.xpath("//div[@class='Lbox DownBtnbox']/a[last()]/@href").extract()
        yield scrapy.Request(href[0], callback=self.getdloadurl)

    def getdloadurl(self, response):
        item = MyspiderItem()
        storyname = response.xpath("//div[@class='Mp3ErweimaText']/p/span/text()").extract()
        stroyDLK = response.xpath("//div[@class='downloadboxlist']/p/a/@href").extract()
        item['name'] = storyname[0]
        item['linkDX'] = stroyDLK[0]
        item['linkLT'] = stroyDLK[1]
        # print(item)
        return item
