# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppItem(scrapy.Item):
    apk_url = scrapy.Field()
    name = scrapy.Field()
    rate = scrapy.Field()
    category = scrapy.Field()
    size = scrapy.Field()
    url = scrapy.Field()
    screenshots = scrapy.Field()
    download_num = scrapy.Field()


class GoogleItem(scrapy.Item):
    url = scrapy.Field()
    # num = scrapy.Field()
    # title = scrapy.Field()
    # description = scrapy.Field()
    table_title = scrapy.Field()
    title = scrapy.Field()
    title_url = scrapy.Field()
    img_url = scrapy.Field()
    description = scrapy.Field()
    developer = scrapy.Field()
    developer_url = scrapy.Field()
    price = scrapy.Field()
    _id = scrapy.Field()
    download_range = scrapy.Field()
    category = scrapy.Field()
    # 内容分级
    content_rating = scrapy.Field()
    operating_systems = scrapy.Field()
    current_version = scrapy.Field()
    file_size = scrapy.Field()
    publish_date = scrapy.Field()
    rating_count = scrapy.Field()
    current_rate = scrapy.Field()


class HiapkItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    info = scrapy.Field()
    apk_url = scrapy.Field()
