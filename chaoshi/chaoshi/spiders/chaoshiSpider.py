# -*- coding: utf-8 -*-
import scrapy
import time

class ChaoshispiderSpider(scrapy.Spider):
    name = "chaoshi"
    allowed_domains = ["jd.com", "3.cn"]
    start_urls = (
        'http://chaoshi.jd.com/?t=%s' % str(int(time.time() * 1000)),
    )

    def parse(self, response):
        # print(response.body)
        # with open('a.html', 'wb') as f:
        #     f.write(response.body)
        # print response.url
        for sub_cate2_href in response.xpath('//div[@class="sub-cate2"]/a'):
            print sub_cate2_href.xpath('@href').extract()
            print sub_cate2_href.xpath('text()').extract()
