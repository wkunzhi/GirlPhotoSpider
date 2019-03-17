# -*- coding: utf-8 -*-

import scrapy


class PicsDownloadItem(scrapy.Item):

    image_urls = scrapy.Field()  # 图片的下载地址， 该字段是存储图片的列表
    image_path = scrapy.Field()  # 图片本地存储路径(相对路径)
