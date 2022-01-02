#!/usr/bin/python
# -*- coding: UTF-8 -*-
from lxml import etree

# 读取文章题目，取出名称和数据
def readTopic():
    try:
        openFile = open("./网页设计与制作.html", "r")
        data = openFile.read()
        html = etree.HTML(data)
        for element in html.xpath('//div[@class="st_xx"]'):
            print(element)
        print(len(html.xpath('//div[@class="st_xx"]')))
        print(len(html.xpath('//div[@class="st_tm"]')))
    finally:
        openFile.close()

if __name__ == "__main__":
    readTopic()
