# -*- coding: utf-8 -*-
"""
used for jd.com

"""

# modelUrl = "http://p.3.cn/prices/mgets?type=1&skuIds=J_10021886013"
import requests
import json
modelUrl = "http://p.3.cn/prices/mgets?type=1&skuIds=%s"


headers = {
    "Host": "p.3.cn",
    "Connection": "keep-alive",
    "Cache-Control": "no-cache",
    "Accept": "*/*",
    "Pragma": "no-cache",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36",
    "DNT": "1",
    "Referer": "http://list.jd.com/list.html",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",

}

def priceQuery(itemId):
    """
    get item price using itemId

    return {u'p': u'-1.00', u'm': u'-1.00', u'id': u'J_100218860133'}
    if itemId not exsit
    """
    url = modelUrl % itemId
    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.ok and resp.text:
        return json.loads(resp.text)[0]
    else:
        return {u'p': u'-1.00', u'm': u'-1.00', u'id': u'J_100218860133'}

if __name__ == '__main__':
    print(priceQuery('J_10021886013'))
