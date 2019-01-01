
Scrapy-redis 项目



一 程序运行：
Master 端打开Redis： redis-server 
Slave 端运行爬虫： scrapy carwl youyuan
多个 Slave 端运行爬虫顺序没有限制


二 改写为分布式爬虫：
RedisCrawlSpider 类，并在多个Slave 端运行

三 分布式爬虫执行方式：
1  Master: redis-server
2  Slave:  scrapy runspider youyuan.py
3  在Master 端的 redis-cli 里push 一个 start_urls
   redis-cli> lpush youyuan:start_urls http://www.youyuan.com/find/beijing/mm18-25/advance-0-0-0-0-0-0-0/p1/

4  爬虫启动，查看 redis 数据库数据
5  处理 Redis 里数据： process_item.py 文件中自定义编写


四 数据存储 MongoDB
1  启动 MongoDB 数据库： sudo mongod 
2  执行程序： python(py2) process_youyuan_mongodb.py 
3  MongoDB 可视化管理工具： adminMongo
   安装地址：https://github.com/mrvautin/adminMongo

五 数据存储 MySQL
1  启动mysql:  mysql.server start (Linux下: server mysql start )
2  登陆到 root用户： mysql -uroot -p 
3  创建数据库youyuan: create database youyuan;
4  切换到指定数据库：  use youyuan;
5  创建表beijingGirl以及所有字段的列名和数据类型： 可视化管理工具创建
    MySQL可视化工具： Navicat 或 phpMyAdmin

6  执行程序： py2 process_youyuan_mysql.py





