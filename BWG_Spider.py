#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import re
from lxml import html


def saveAsTemp(content, path):
    f = open(path, 'w')
    f.write(content)
    f.close()


def readFromFile(path):
    f = open(path, 'r')
    return f.read()


def re_search(reg, text):
    ram_re = re.search(reg, text)
    if ram_re:
        ram = ram_re.group(1)
        return ram.strip()


url = "https://bandwagonhost.com/cart.php"


def getProductListFromHomePage():
    pruductMap = {}

    print u"开始爬取数据"
    r = requests.get(url)

    htmlContent = r.content

    htmlSource = html.fromstring(htmlContent)
    eleList = htmlSource.xpath('//*[@id="order-web20cart"]/div')
    for element in eleList:
        tableElementList = element.xpath("./table")
        if (len(tableElementList) > 0):
            tableElement = element.xpath("./table")[0]
            prudoctName = tableElement.xpath("./tr/td[1]/strong")[0].text_content()
            prudoctInfo = tableElement.xpath("./tr/td[1]")[0].text_content()
            priceContent = tableElement.xpath("./tr/td[2]")[0].text_content()
            canOrder = tableElement.xpath("./tr/td[3]")[0].text_content()

            product = {}
            product["prudoctName"] = prudoctName

            # 当按钮栏显示out of stock的时候表示不能预订
            product["canOrder"] = 'out of stock' not in canOrder
            product["RAM"] = re_search("RAM:(.*)", prudoctInfo)
            product["HDD"] = re_search("HDD:(.*)", prudoctInfo)
            product["CPU"] = re_search("CPU:(.*)", prudoctInfo)
            product["BW"] = re_search("BW:(.*)", prudoctInfo)
            product["Cost_Monthly"] = re_search("(.*)USD Monthly", priceContent)
            product["Cost_Quarterly"] = re_search("(.*)USD Quarterly", priceContent)
            product["Cost_Half_Year"] = re_search("(.*)USD Semi-Annually", priceContent)
            product["Cost_Year"] = re_search("(.*)USD Annually", priceContent)

            pruductMap[prudoctName] = product
            print u"爬取到产品:", prudoctName
    return pruductMap

