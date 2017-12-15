# 实现方法
#使用scrapy多线程异步框架爬取淘宝网商品的数据
#自动翻页：分析搜索结果URL的规律，实现翻页
#获取各商品的URL：使用正则获取各商品的URL并保存在数组中
#获取各商品的“商品名”、“价格”、“链接”等数据

#安装scrapy
#安装MYSQL(php内嵌软件）

'''
在D盘新建文件夹'test'
打开cmd，并执行：
d:
cd /test
d:\scrapy>scrapy startproject taobao #创建名为‘taobao’在工程（项目）
d:\scrapy>cd taobao
d:\scrapy\taobao>scrapy genspider -t basic tb taobao.com #以‘basic’为模版创建名为‘tb’爬虫文件
'''
#用SCRAPY打开'd:\scrapy\taobao\taobao'
#下载‘taobao-spider/spiders/tb.py’，并将其粘贴到SCRAPY的'tb'文件中
#在'setting.py'中将ROBOTSTXT_OBEY = True设置成ROBOTSTXT_OBEY = False
#在'setting.py'中搜索pipelines，将'taobao.pipelines.SomePipeline': 300,设置成‘'taobao.pipelines.TaobaoPipeline': 300,’，并去除前面的#号
#因为文档修改过，所以需要把items.py、piplines.py中的Shop改成Taobao，不然无法正常调用
'''

在cmd中执行爬虫：
d:\scrapy\taobao>scrapy crawl tb --nolog #执行爬虫文件（不加载中间执行过程）
'''

'''
MYSQL查询
show databases;
create database tb;
use tb;
show tables;
create table goods(id int(32) auto_increment primary key,title varchar(100),link varchar(100) unique,price varchar(100),comment varchar(100));
select * from goods;
select * from goods limit 10;
show columns from goods;#查看表goods中所有字段
select count(*) from goods; #goods的条数
'''

#问题1：不能获得所有页的商品ID，可能需要在哪里设置延迟
#问题2：数据无法保存到mysql中
