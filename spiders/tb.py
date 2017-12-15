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

    #爬取商品网页,然后请求URL并交给page函数处理
    def parse(self, response):
        #建立在淘宝上搜索的关键字
        key = '图书'
        #生成搜索“图书”的前10页URL
        for i in range(0, 10):
            #化简URL
            url = 'https://s.taobao.com/search?q='+str(key)+'&imgfile=&commend=all&ie=utf8&s='+str(i*44)
            #通过yield请求URL,并设置回调page函数
            yield Request(url=url, callback=self.page)

    #爬取各商品,然后请求URL并交给next函数处理
    def page(self, response):
        #将各页解码并赋给body变量
        body = response.body.decode('utf-8', 'ignore')
        #在源码中找到商品ID的匹配pattern
        patid = '"nid":"(.*?)"'  # 补充内容
        allid = re.compile(patid).findall(body)
        print(allid) #问题，不能获得所有页的商品ID，可能需要设置延迟
        #获得各商品的RUL
        for j in range(0, len(allid)):
            thisid = allid[j]
            url1 = "https://detail.tmall.com/item.htm?spm=a230r.1.14.9.76bf523ot7cX5&id="+str(thisid)
            yield Request(url=url1, callback=self.next)

  '''
  #执行到page函数就无法继续执行，将调整此测试函数并放在parse函数后面可以执行
    def cesi(self, response):
        print('运行到cesi')
        cesi_url = response.url
        print(cesi_url)
        taobao1 = response.body.decode('utf-8', 'ignore')
        fh = open('D:/可删/taobao2.html', 'w', encoding='utf-8')
        fh.write(taobao1)
        fh.close()
        yield Request(url=cesi_url, callback=self.next)
    '''    
    #爬取商品名、商品链接、商品价格、商品评价数，并通过实例化item将他们保存
    def next(self, response):
        # 实例化item保存爬取的数据
        item = TaobaoItem()
        item['title'] = response.xpath('//meta[@name="keywords"]/@content')
        item['link'] = response.url
        pat_price = '"defaultItemPrice":"(.*?)"'
        item['price'] = re.compile(pat_price).findall(response.body.decode('utf-8','ignore'))
        pat_id = 'id=(.*?)$'
        #由于不能直接在源码中打到评论数，使用fiddler抓包（在JS文件中）得到评价数URL规律
        id_comment = re.compile(pat_id).findall(response.url)[0]
        url_comment = 'https://rate.tmall.com/list_dsr_info.htm?itemId='+str(id_comment)
        print(url_comment)
        #解决SSL错误
        ssl._create_default_https_context=ssl._create_unverified_context()
        commentdata = urllib.request.urlopen(url_comment).read().decode('utf-8','ignore')
        pat_comment = '"rateTotal":(.*?),"'
        item['comment'] = re.compile(pat_comment).findall(commentdata)
        yield item
