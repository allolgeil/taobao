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
    key = ''
