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
from settings import SPIDERPATH

class ChaoshiCategoryPipeline(object):
    def __init__(self):
        saveDir = os.path.join(SPIDERPATH, 'output')
        fileName = timestamp() + '.json'
        self.jsonFile = open(builDir(saveDir, fileName), 'wb')

    def process_item(self, item, spider):
        """
        处理和保存超市二级目录的url
        """
        line = json.dumps(dict(item)) + '\n'
        self.jsonFile.write(line)
        return item


# saveDir = os.path.join(SPIDERPATH, 'output')
# fileName = timestamp() + '.json'
# jsonFile = open(builDir(saveDir, fileName), 'wb')
