# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 爬取封面图片
class ImagespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    img_url = scrapy.Field()
    link_url = scrapy.Field()

class ChinazItem(scrapy.Item):
    title = scrapy.Field()
    img_url = scrapy.Field()
    link_url = scrapy.Field()
    download_url = scrapy.Field()
    detail_img = scrapy.Field()
    image_paths = scrapy.Field()
    description = scrapy.Field()
    type = scrapy.Field()


# 爬取京东书籍信息
class JdBookItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    description = scrapy.Field()
    author = scrapy.Field()
    book_image = scrapy.Field()
    content = scrapy.Field()
    score = scrapy.Field()
    delete = scrapy.Field()
    created_at = scrapy.Field()
    updated_at = scrapy.Field()
    type = scrapy.Field()


# 爬取详情
class ImagesDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    img_url = scrapy.Field()
    link_url = scrapy.Field()

# 图虫获取图片
class TucongItem(scrapy.Item):
    img_url = scrapy.Field()
    img_id = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()