# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import sys
import pymysql
from datetime import datetime
# python >3.4
import importlib

importlib.reload(sys)

# 导入数据库模块
# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "123456", "web_site_db")
# 使用cursor()方法获取操作游标
cursor = db.cursor()


class ImageSpiderPipeline(object):
    def __init__(self):
        self.file = open("/Users/aming/testFile/dynamic_theme/document/network_image.json", 'w')

    def process_item(self, item, spider):
        print(item, '----------------------OOOo')
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.file.write(content)
        return item

    def close_spider(self, spider):
        self.file.close()


# 保存图片
class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        print(item, '----------------------OOO')
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'gzip, deflate, br',
            'Cache-Control': 'max-age=0',
            # 'Host': 'img1.mm131.me',
            'If-Modified-Since': 'Wed, 28 Mar 2018 14:33:26 GMT',
            'If-None-Match': 'dbd856dbbc993f131420942feeccc56a',
            # 'Proxy-Connection': 'keep-alive',
            # 'Referer': 'https://photo.tuchong.com/',
            'Upgrade-Insecure-Requests': 1,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
        }
        yield scrapy.Request(item['img_url'])

    def item_completed(self, results, item, info):
        # image_paths = [x['path'] for ok, x in results if ok]
        # if not image_paths:
        #     raise DropItem("Item contains no images")
        # item['image_paths'] = image_paths
        return item


# 爬取站长素材的,保存图片
class FreePsdPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # print item['detail_img']
        yield scrapy.Request(item['detail_img'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        # SQL 插入语句 数据库相关,看个人的需求
        # sql = "INSERT INTO site_psd_info(title, \
        #     image_url, link_url, local_url, download_url, description, type, date_time) \
        #     VALUES ('%s', '%s', '%s', '%s', '%s', '%s','%s', '%s')" % \
        #     (item['title'], item['img_url'], item['link_url'], image_paths[0][5:], item['download_url'], item['description'], item['type'], int(round(time.time() * 1000)))
        # try:
        # # 执行sql语句
        #     cursor.execute(sql)
        #     # 提交到数据库执行
        #     db.commit()
        # except:
        # # 如果发生错误则回滚
        #     db.rollback()
        # print(results, image_paths, '---------------4545')
        # if not image_paths:
        #     raise DropItem("Item contains no images")
        # item['image_paths'] = image_paths
        return item


# 爬取京东网站上的书籍
class JdBookWebPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['book_image'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        # SQL 插入语句 数据库相关,看个人的需求
        sql = "INSERT INTO site_app_book(title, \
            description, author, book_image, content, created_at, updated_at) \
            VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
              (item['title'], item['description'], item['author'], image_paths[0][5:], item['content'],
               datetime.now().strftime('%Y-%m-%d %H:%M:%S'), datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except Exception as error:
            # 如果发生错误则回滚
            print(error, '---------------error')
            db.rollback()
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
