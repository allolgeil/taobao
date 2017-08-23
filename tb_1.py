# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import ssl
from scrapy.http import Request
import re
from taobao.items import TaobaoItem

class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['taobao.com']
    start_urls = ['http://taobao.com/']

    def parse(self, response):
        key = '图书'
        for i in range(0, 10):
            url = 'https://s.taobao.com/search?q='+str(key)+'&imgfile=&commend=all&ie=utf8&s='+str(i*44)
            yield Request(url=url, callback=self.page)

    def page(self, response):
        body = response.body.decode('utf-8', 'ignore')
        patid = '"nid":"(.*?)"'  # 补充内容
        allid = re.compile(patid).findall(body)
        print(allid)
        for j in range(0, len(allid)):
            thisid = allid[j]
            url1 = "https://detail.tmall.com/item.htm?spm=a230r.1.14.9.76bf523ot7cX5&id="+str(thisid)
            yield Request(url=url1, callback=self.next)

    def next(self, response):
        item = TaobaoItem()
        item['title'] = response.xpath('//meta[@name="keywords"]/@content')
        item['link'] = response.url
        pat_price = '"defaultItemPrice":"(.*?)"'
        item['price'] = re.compile(pat_price).findall(response.body.decode('utf-8','ignore'))
        pat_id = 'id=(.*?)$'
        id_comment = re.compile(pat_id).findall(response.url)[0]
        url_comment = 'https://rate.tmall.com/list_dsr_info.htm?itemId='+str(id_comment)
        print(url_comment)
        ssl._create_default_https_context=ssl._create_unverified_context()
        commentdata = urllib.request.urlopen(url_comment).read().decode('utf-8','ignore')
        pat_comment = '"rateTotal":(.*?),"'
        item['comment'] = re.compile(pat_comment).findall(commentdata)
        yield item
