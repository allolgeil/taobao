# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import random
from scrapy.http import Request
import re
from lxml import etree
from taobao.items import TaobaoItem


class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['taobao.com']
    '''
    def start_requests(self):
        key = urllib.request.quote('图书')
        ua = [
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3831.602 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/55.0',
            'Opera/9.27 (Windows NT 5.2; U; zh-cn)', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)']
        for i in range(0,5):
            start_urls = 'https://s.taobao.com/search?q='+str(key)+'&imgfile=&commend=all&ie=utf8&s='+str(i*44)
            #print(start_urls)
            req = urllib.request.Request(start_urls)
            req.add_header('User-Agent',random.choice(ua))
            data = urllib.request.urlopen(req).read().decode('UTF-8','ignore')
           
            fh = open('d:/可删/req1.html','w',encoding='UTF-8')
            fh.write(data)
            fh.close()
          
            yield Request(url=start_urls,callback=self.parse)
        print(len(data))
    def parse(self, response):
        body = response.body.decode('utf-8', 'ignore')
        patid = '"nid":"(.*?)"'
        allid = re.compile(patid).findall(body)
        print(len(allid))
        print(allid)
        for j in range(0, len(allid)):
            thisid = allid[j]
            url1 = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.9.76bf523ot7cX5&id='+str(thisid)
            yield Request(url=url1, callback=self.shafa)
    def shafa(self,response):
        pass
    '''


    def start_requests(self):
        key = urllib.request.quote('图书')
        start_urls = 'https://s.taobao.com/search?q=' + str(key) + '&imgfile=&commend=all&ie=utf8&s=' + str(44)
        print(start_urls)
        req = urllib.request.urlopen(start_urls).read().decode('utf-8', 'ignore')
        #body = response.body.decode('utf-8', 'ignore')
        patid = '"nid":"(.*?)"'
        allid = re.compile(patid).findall(req)
        print(len(allid))
        for j in range(0, len(allid)):
            thisid = allid[j]
            url1 = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.9.76bf523ot7cX5&id='+str(thisid)
            yield Request(url=url1, callback=self.shafa)
    def shafa(self,response):
        link = response.url
        print(link)
        title = response.xpath('//meta[@name="keywords"]/@content')
        print(title)
        pat_price = '"defaultItemPrice":"(.*?)"'
        price = re.compile(pat_price).findall(response.body.decode('utf-8', 'ignore'))
        print(price)
        pat_id = 'id=(.*?)$'
        id_comment = re.compile(pat_id).findall(response.url)[0]
        url_comment = 'https://rate.tmall.com/list_dsr_info.htm?itemId=' + str(id_comment)
        #print(url_comment)
        commentdata = urllib.request.urlopen(url_comment).read().decode('utf-8', 'ignore')
        pat_comment = '"rateTotal":(.*?),"'
        comment = re.compile(pat_comment).findall(commentdata)
        print(comment)

        item = TaobaoItem()
        item['title'] = response.xpath('//meta[@name="keywords"]/@content')
        item['link'] = response.url
        pat_price = '"defaultItemPrice":"(.*?)"'
        item['price'] = re.compile(pat_price).findall(response.body.decode('utf-8', 'ignore'))
        pat_id = 'id=(.*?)$'
        # 由于不能直接在源码中打到评论数，使用fiddler抓包（在JS文件中）得到评价数URL规律
        id_comment = re.compile(pat_id).findall(response.url)[0]
        url_comment = 'https://rate.tmall.com/list_dsr_info.htm?itemId=' + str(id_comment)
        print(url_comment)
        # 解决SSL错误
        ssl._create_default_https_context = ssl._create_unverified_context()
        commentdata = urllib.request.urlopen(url_comment).read().decode('utf-8', 'ignore')
        pat_comment = '"rateTotal":(.*?),"'
        item['comment'] = re.compile(pat_comment).findall(commentdata)
        yield item
