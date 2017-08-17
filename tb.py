import scrapy
import urllib.request
import ssl
import scrapy.http import Request
import re
from shop.item import ShopItem

class Tbpider(scrapy.Spider):
  name = 'tb'
  allowed_domains = ['taobao.com']
  start_urls = ('https://www.taobao.com/')
  
  def parse(self,response):
    key = '图书'
    for i in range(0,10):
      url = ''#补充内容
      yield Request(url=url,callback=self.page)
  
  def page(self,response):
    body = response.body.decode('utf-8','ignore')
    patid = ''#补充内容
    allid = re.compile(patid).findall(body)
    print(allid)
    for j in range(0,len(allid)):
      thisid = allid[j]
      url1 = ""#补充内容
      yield Request(url=url,callback=self.next)
      
  def next(self,response):
    item = ShopItem()
    item['title'] = response.xpath("")#补充内容
    item['link'] = response.url
    item['price']= response.xpath('')#补充内容
    '''
    '''
    yield item
