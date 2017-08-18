#-*- coding:utf-8 -*-
import pymysql

class ShopPipeline(object):
  def __init__(self):
    self.conn = pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='tb')
  def process_item(self,item,spider):
    try:
      title = item['title'][0]
      link = item['link']
      price = item['price'][0]
      comment = item['comment'][0]
      sql = "insert into goods(title,link,price,comment)values('"+title+"','"+link+"','"+price+"','"+comment+"')"
      self.conn.query(sql)
      print(title)
      print(link)
      print(price)
      print(comment)
      return item
    except Exception as e:
      pass
  def close_spider(self):
    self.conn.close()
