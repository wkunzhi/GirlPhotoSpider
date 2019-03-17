# -*- coding: utf-8 -*-
import scrapy
from GirlPhotoSpider.items import PicsDownloadItem

"""
pip install pillow 
"""


class GetGirlSpider(scrapy.Spider):
    name = 'get_girl'
    start_urls = ['https://www.meitulu.com/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'GirlPhotoSpider.pipelines.PicsDownloadPipeline': 300,

        },
        'DEFAULT_REQUEST_HEADERS': {
            'Referer': 'https://www.meitulu.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        },
        'IMAGES_STORE': './photo',
        # 90天的图片失效期限
        # 'IMAGES_EXPIRES': 90,
        # 启用AutoThrottle扩展
        # 'AUTOTHROTTLE_ENABLED': True,
        # 初始下载延迟(单位:秒)
        # 'AUTOTHROTTLE_START_DELAY': 10,
        # 在高延迟情况下最大的下载延迟(单位秒)
        # 'AUTOTHROTTLE_MAX_DELAY': 60,
    }

    def parse(self, response):
        self.log(response.headers)
        # 获取所有的图片, 以列表形式保存到 image_urls 字段中。
        pic_list = response.xpath("/html/body/div[3]/div[8]/ul/li/a/img/@src").extract()  # extract() 传入 列表
        print('开始咯===========')
        print(pic_list)
        if pic_list:
            item = PicsDownloadItem()
            item['image_urls'] = pic_list
            yield item
