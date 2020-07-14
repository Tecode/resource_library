import json

import scrapy


class TucongSpider(scrapy.Spider):
    name = 'tucong'
    allowed_domains = ['https://tuchong.com']
    params = [
        '人像'
        '小清新',
        '女孩',
        '日系',
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
                    base_url = 'https://photo.tuchong.com/';
                    print(
                        base_url + str(item_data['author_id']) + '/f/' + str(img_data['img_id']) + '.jpg')
            self.page += 1
            yield scrapy.Request(self.get_url(), callback=self.parse, dont_filter=True)
        else:
            self.start_index += 1
            self.page = 1
            yield scrapy.Request(self.get_url(), callback=self.parse, dont_filter=True)
