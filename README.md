# taobao
#使用scrapy多线程异步框架爬取淘宝网商品的数据
#自动翻页：分析搜索结果URL的规律，实现翻页
#获取各商品的URL：使用正则获取各商品的URL并保存在数组中
#获取各商品的“商品名”、“价格”、“链接”等数据
#

#coding:utf-8
'''
d:\scrapy>scrapy startproject taobao
d:\scrapy>cd taobao
d:\scrapy\taobao>scrapy genspider -t basic tb taobao.com
d:\scrapy\taobao>scrapy crawl tb --nolog
'''



'''
show databases;
create database tb;
use tb;
show tables;
create table goods(id int(32) auto_increment primary key,title varchar(100),link varchar(100) unique,price varchar(100),comment varchar(100));
select * from goods;
select * from goods limit 10;
show columns from goods;#查看表goods中所有字段
'''
select count(*) from goods; #goods的条数
