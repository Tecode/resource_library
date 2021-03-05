import scrapy
from resource_library.items import ImagespiderItem

class Mm131Spider(scrapy.Spider):
    name = 'm311'
    allowed_domains = ['www.mm131.com']
    offset = 1
    base_url = 'http://www.mm131.com/xinggan/'
    start_urls = ['http://www.mm131.com/xinggan/']

    def parse(self, response):
        nodes = response.xpath(
            '//dl[@class="list-left public-box"]/dd[not(@class)]')
        for node in nodes:
            item = ImagespiderItem()
            item['title'] = node.xpath('./a/text()').extract()[0]
            item['img_url'] = node.xpath('./a/img[1]/@src').extract()[0]
            item['link_url'] = node.xpath('./a/@href').extract()[0]
            yield item

        if self.offset < 127:
            self.offset += 1
            url = self.base_url + 'list_6_' + str(self.offset) + '.html'
            yield scrapy.Request(url, callback=self.parse)
