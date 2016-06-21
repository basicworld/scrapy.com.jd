# -*- coding: utf-8 -*-
import scrapy
import time
from chaoshi.items import ChaoshiGoodsItem


class ChaoshispiderSpider(scrapy.Spider):
    name = "chaoshi"
    allowed_domains = ["jd.com", "3.cn"]
    start_urls = (
        'http://chaoshi.jd.com/?t=%s' % str(int(time.time() * 1000)),
    )

    def parse(self, response):
        """
        获取超市的二级目录
        通过目录就可以获得目录下的所有商品
        """
        # print(response.body)
        # with open('a.html', 'wb') as f:
        #     f.write(response.body)
        # print response.url
        for sub_cate2_href in response.xpath('//div[@class="sub-cate2"]/a'):
            # item = ChaoshiCategoryItem()
            # item['cateUrl'] = sub_cate2_href.xpath('@href').extract_first()
            cateName = sub_cate2_href.xpath('text()').extract_first()
            # print cateName
            url = sub_cate2_href.xpath('@href').extract_first()
            url = response.urljoin(url)
            print(url)
            # yield item
            yield scrapy.Request(url, callback=self.parseCategory)

    def parseCategory(self, response):
        """
        # 遍历每个二级目录下的商品
        """
        xpathDict = {
            'goodsName': 'div[@class="p-name p-name-type-2"]/a/@title',
            'goodsId': 'div[@class="p-name p-name-type-2"]/a/i[@class="promo-words"]/@id',
            'goodsUrl': 'div[@class="p-name p-name-type-2"]/a/@href',
            'goodsPrice': 'div[@class="p-price"]/strong/i/text()',
            'goodsPicUrl': 'div[@class="p-img"]/a/@href',
        }
        for sel in response.xpath('//li[@class="gl-item"]/div'):
            item = ChaoshiGoodsItem()
            for itemName, itemXpath in xpathDict.items():
                item[itemName] = sel.xpath(itemXpath).extract_first()
            yield item

        url = response.url
        headers = response.headers
        headers['Referer'] = url
