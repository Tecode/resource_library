import json

import scrapy

from resource_library.items import TucongItem


class TucongSpider(scrapy.Spider):
    name = 'tucong'
    allowed_domains = ['tuchong.com', 'photo.tuchong.com']
    params = [
        '写真',
    ]
    start_index = 0
    page = 1

    def get_url(self):
        print(self.params[self.start_index])
        print(self.page)
        return "https://tuchong.com/rest/tags/{}/posts?page={}&count={}&order=weekly&before_timestamp=".format(
            self.params[self.start_index], self.page, 20)

    def start_requests(self):
        yield scrapy.Request(self.get_url(), callback=self.parse)

    def parse(self, response):
        # 获取到的json数据
        json_data = json.loads(response.body)
        if json_data['more'] and self.page < 100:
            for item_data in json_data['postList']:
                for img_data in item_data['images']:
                    base_url = 'https://photo.tuchong.com/'
                    item = TucongItem()
                    item['img_url'] = base_url + str(item_data['author_id']) + '/f/' + str(img_data['img_id']) + '.jpg'
                    item['width'] = img_data['width']
                    item['height'] = img_data['height']
                    item['img_id'] = img_data['img_id']
                    yield item
            self.page += 1
            yield scrapy.Request(self.get_url(), callback=self.parse)
        else:
            self.start_index += 1
            self.page = 1
            yield scrapy.Request(self.get_url(), callback=self.parse)
