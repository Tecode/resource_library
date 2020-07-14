import scrapy
from datetime import datetime
from scrapy_splash import SplashRequest
from resource_library.items import JdBookItem


class JingDongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['s-e.jd.com', 'e.jd.com', 'dx.3.cn']
    start_urls = ['https://s-e.jd.com/Search']
    offset = 1
    base_url = 'https://s-e.jd.com/Search?key=%E7%BC%96%E7%A8%8B&enc=utf-8&wq=%E7%BC%96%E7%A8%8B&psort=3&page='

    # request需要封装成SplashRequest

    def start_requests(self):
        url = self.base_url + str(self.offset) + '#J_filter'
        yield scrapy.Request(url, callback=self.parse)

    # 获取列表,一个一个的列表,之后获取详情
    def parse(self, response):
        nodes = response.xpath('//div[@class="gl-i-wrap"]')
        for node in nodes:
            link_url = node.xpath(
                './div[@class="p-name"]/a/@href').extract()[0]
            if link_url and link_url.find('//e.jd') > -1:
                yield SplashRequest('https:' + link_url, self.detail, args={'wait': '1.5'})

        if self.offset < 34:
            self.offset += 1
            url = self.base_url + str(self.offset) + '#J_filter'
            print(url, '----------------------------------------------url')
            yield scrapy.Request(url, callback=self.parse)

    # 获取详情,获取书籍的内容已经大图
    def detail(self, response):
        item = JdBookItem()
        # 书籍封面
        small_image = response.xpath(
            '//img[@id="spec-img"]/@data-origin').extract()[0]
        item['book_image'] = 'https:' + small_image
        # 标题
        item['title'] = response.xpath(
            '//div[@class="sku-name"]/text()').extract()[0]
        # 描述
        item['description'] = response.xpath(
            '//div[@id="contentInfo"]/div[@class="con"]/text()').extract()[0]
        # 作者
        item['author'] = response.xpath(
            '//div[@class="author"]/a/text()').extract()[0]
        # 文章内容
        item['content'] = response.xpath(
            '//div[@id="digest"]/div[@class="con"]/text()').extract()[0]
        item['score'] = 5
        item['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        item['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(item)
        yield item
