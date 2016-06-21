# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
# import sys
# from os.path import dirname
# SPIDERPATH = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
# sys.path.append(SPIDERPATH)
from scrapyUtils.xutils.xbuild import builDir
from scrapyUtils.xutils.xtime import timestamp
from scrapyUtils.xutils.xlsx import XlsxWriter
from settings import SPIDERPATH
from collections import OrderedDict

class ChaoshiCategoryPipeline(object):
    def __init__(self):
        saveDir = os.path.join(SPIDERPATH, 'output', 'category')
        fileName =  'chaoshiCategory' + timestamp() + '.json'
        self.jsonFile = open(builDir(saveDir, fileName), 'wb')

    def process_item(self, item, spider):
        """
        处理和保存超市二级目录的url
        """
        line = json.dumps(dict(item)) + '\n'
        self.jsonFile.write(line)
        return item


class ChaoshiGoodsPipeline(object):
    def __init__(self):
        saveDir = os.path.join(SPIDERPATH, 'output', 'goods')
        fileName = 'chaoshiGoods' + timestamp() + '.json'
        self.jsonFile = open(builDir(saveDir, fileName), 'wb')

        fileName2 = 'chaoshiGoods' + timestamp() + '.xlsx'
        self.xlsxFile = XlsxWriter(builDir(saveDir, fileName2), saveDir)
        self.xlsxWriteTitle = 1

    def process_item(self, item, spider):
        """
        处理和保存产品
        """
        if item['goodsId']:
            line = json.dumps(dict(item)) + '\n'
            self.jsonFile.write(line)
            if self.xlsxWriteTitle:
                self.xlsxWriteTitle = 0
                self.xlsxFile.writeRow(OrderedDict(item).keys())
            self.xlsxFile.writeRow(OrderedDict(item).values())
            return item

# saveDir = os.path.join(SPIDERPATH, 'output')
# fileName = timestamp() + '.json'
# jsonFile = open(builDir(saveDir, fileName), 'wb')
