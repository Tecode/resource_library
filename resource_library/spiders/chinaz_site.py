import scrapy
from resource_library.items import ChinazItem


class ChinazSiteSpider(scrapy.Spider):
    name = 'chinaz'
    allowed_domains = ['sc.chinaz.com']
    start_urls = ['http://sc.chinaz.com/psd/free.html#/']
    base_url = 'http://sc.chinaz.com/psd/free'
    offset = 1

    def parse(self, response):
        nodes = response.xpath('//div[@class="box col3 ws_block"]')
        for node in nodes:
            item = ChinazItem()
            item['title'] = node.xpath('./p/a/text()').extract()[0]
            item['img_url'] = node.xpath('./a[1]/img/@src').extract()[0]
            link_url = node.xpath('./a/@href').extract()[0]
            item['link_url'] = link_url
            if link_url and link_url.find('http://') > -1:
                yield scrapy.Request(link_url, meta={'item':item}, callback=self.detail)

        if self.offset < 2:
            self.offset += 1
            url = self.base_url + '_' + str(self.offset) + '.html'
            yield scrapy.Request(url, callback=self.parse)

    def detail(self, response):
        item = response.meta['item']
        item['detail_img'] = response.xpath('//div[@class="show_warp jl_warp clearfix"]/img/@src').extract()[0]
        item['description'] = response.xpath('//div[@class="intro clearfix pb10"]/p/text()').extract()[0]
        item['type'] = response.xpath('//div[@class="time fl"]/span/a/text()').extract()[0]
        hrefs = response.xpath('//div[@class="clearfix mt20 downlist"]/ul/li')
        url = ''
        for href in hrefs:
            url += href.xpath('./a/@href').extract()[0] + ','
        item['download_url'] = url
        # print item;
        yield item