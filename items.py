#-*-coding:utf-8-*-
import scrapy
class ShopItem(scrapy.Item):
  title = scrapy.Field()
  link = scrapy.Field()
  price = scrapy.Field()
  comment = scrapy.Field()
