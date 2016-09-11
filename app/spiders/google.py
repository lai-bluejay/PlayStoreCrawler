# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
import requests
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from app.items import GoogleItem
from scrapy.selector import Selector
import re


class GoogleSpider(CrawlSpider):
    name = "google"
    allowed_domains = ["play.google.com"]
    start_urls = [
        'https://play.google.com/store/apps',
        'https://play.google.com/store/apps/details?id=com.facebook.katana'
    ]
    rules = [
        Rule(LinkExtractor(allow=("https://play\.google\.com/store/apps/details",)), callback='parse_app', follow=True),
    ]  # CrawlSpider 会根据 rules 规则爬取页面并调用函数进行处理

    # def parse(self, response):
    #       #取得 顯示更多內容 URL
    #       for url in response.xpath('//a[@class="see-more play-button small id-track-click apps id-responsive-see-more"]'):
    #           targetURL = "https://play.google.com" + url.xpath('@href')[0].extract()
    #           #使用POST , 抓資料 100 筆
    #           yield  scrapy.FormRequest(
    #                  targetURL,
    #                  formdata = {'start':'0',
    #                              'num':'100',
    #                              'numChildren':'0',
    #                              'cctcss':'square-cover',
    #                              'cllayout':'NORMAL',
    #                              'ipf':'1',
    #                              'xhr':'1',
    #                              'token':'zNTXc17yBEzmbkMlpt4eKj14YOo:1458833715345'},
    #                 callback = self.parse_app
    #              )

    def parse_app(self, response):
        # 获取页面的 URL 以及下载数量
        item = GoogleItem()
        # item = dict()
        google_selector = Selector(response)
        item['title'] = response.xpath("//div[@class='id-app-title']").xpath("text()").extract()[0]
        idg = re.search('id=(\w+\.\w+\.\w+)', response.url)
        item['_id'] = idg.group(1)
        item['url'] = "https://play.google.com/store/apps/details?id="+item["_id"]
        item['download_range'] = response.xpath("//div[@itemprop='numDownloads']").xpath("text()").extract()[0]
        item['developer'] = google_selector.xpath("//span[@itemprop='name']/text()").extract()
        item['category'] = google_selector.xpath("//span[@itemprop='genre']/text()").extract()
        # app的描述是一段文字，在<p>标签里面
        des_divs = google_selector.xpath("//div[@jsname='C4s9Ed']").xpath("string(.)").extract()[0]
        des_string = des_divs
        # for p in des_divs.xpath('.//p'):
        #     tmp = p.xpath("text()").extract()[0]
        #     des_string += tmp
        item['description'] = des_string
        try:
        # 打分
            item['current_rate'] = google_selector.xpath("//div[@class='score-container']/meta[1]/@content").extract()[0]
            # 打分人数
            item['rating_count'] = google_selector.xpath("//div[@class='score-container']/meta[2]/@content").extract()[0]
        except:
            item['current_rate'] = 'no rate'
            item['rating_count'] = 0
        # 其他详情
        try:
            item['publish_date'] = google_selector.xpath("//div[@itemprop='pulbilshDate']/text()").extract()[0]
        except:
            item['publish_date'] = google_selector.xpath("//div[@itemprop='datePublished']/text()").extract()[0]
        item['file_size'] = google_selector.xpath("//div[@itemprop='fileSize']/text()").extract()[0]
        item['current_version'] = google_selector.xpath("//div[@itemprop='softwareVersion']/text()").extract()[0]
        item['operating_systems'] = google_selector.xpath("//div[@itemprop='operatingSystems']/text()").extract()[0]
        item['content_rating'] = google_selector.xpath("//div[@itemprop='contentRating']/text()").extract()[0]
        price = google_selector.xpath("//button[@class='price buy id-track-click id-track-impression']/span[2]/text()").extract()[0]
        item['price'] = price
        item['img_url'] = google_selector.xpath("//div[@class='cover-container']/img/@src").extract()[0]
        item['developer_url'] = "https://play.google.com/store/apps/developer?" + google_selector.xpath("//div[@itemprop='author']/meta/@content").extract()[0]
        #TODO 权限需要, 内购价格
        # other_details = google_selector.xpath()

        yield item
