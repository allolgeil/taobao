# taobao
#coding:utf-8
'''
d:\scrapy>scrapy startproject taobao
d:\scrapy>cd taobao
d:\scrapy\taobao>scrapy genspider -t basic tb taobao.com
'''

'''
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
