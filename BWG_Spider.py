#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import re
from common import FileUtil
from BeautifulSoup import BeautifulSoup


def re_search(reg, text, index):
    ram_re = re.search(reg, text)
    if ram_re:
        ram = ram_re.group(index)
        return ram.strip()


url = "https://bandwagonhost.com/cart.php"


def getProductListFromHomePage():
    pruductMap = {}

    print u"开始爬取数据"
    r = requests.get(url)

    htmlContent = r.content

    soup = BeautifulSoup(htmlContent)
    tableList = soup.findAll(attrs={'class': re.compile(r".*\bnoborders\b.*")})
    for tb in tableList:
        print "--------------------------------------"
        productInfo = str(tb.contents[1].contents[1])
        priceInfo = str(tb.contents[1].contents[3])

        product = {}
        prudoctName = re_search("<strong>(.*)</strong>", productInfo, 1)
        product["prudoctName"] = prudoctName

        count = "0"
        canOrder = False
        if "<em>" in productInfo:
            enInfo = re_search("<em>(.*)</em>", productInfo, 1)
            if "(out of stock)" == enInfo:
                # 如果em元素中包含out of stock，表示已经售完
                canOrder = False
                count = "0"
            else:
                # 如果em元素中包含5 avlivale，表示还剩余一定的数量
                canOrder = True
                count = enInfo
        else:
            canOrder = True
            count = ""

        product["canOrder"] = canOrder
        product["AvaliableCount"] = count
        product["RAM"] = re_search("RAM:(.*)[<]", productInfo, 1)
        product["HDD"] = re_search("HDD:(.*)[<]", productInfo, 1)
        product["CPU"] = re_search("CPU:(.*)[<]", productInfo, 1)
        product["BW"] = re_search("BW:(.*)[<]", productInfo, 1)
        product["Cost_Monthly"] = re_search("[$](.*)USD Monthly", priceInfo, 1)
        product["Cost_Quarterly"] = re_search("[$](.*)USD Quarterly", priceInfo, 1)
        product["Cost_Half_Year"] = re_search("[$](.*)USD Semi-Annually", priceInfo, 1)
        product["Cost_Year"] = re_search("[$](.*)USD Annually", priceInfo, 1)
        pruductMap[prudoctName] = product
        print product

        print "--------------------------------------"

    return pruductMap
