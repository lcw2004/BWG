#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import urllib2
import re
import json
import urllib
from lxml import etree as etree
from lxml import html

def saveAsTemp(content, path):
    f = open(path, 'w')
    f.write(content)
    f.close()

def readFromFile(path):
    f = open(path, 'r')
    return f.read()



url = "https://bandwagonhost.com/cart.php"



def start():
    # r = requests.get(url)
    # saveAsTemp(r.content, 'D:\\1.html')

    htmlContent = readFromFile('D:\\1.html')

    htmlSource = html.fromstring(htmlContent)

    eleList = htmlSource.xpath('//*[@id="order-web20cart"]/div')
    print len(eleList)
    for element in eleList:
        tableElementList = element.xpath("./table")
        if(len(tableElementList) > 0):
            tableElement = element.xpath("./table")[0]
            # print tableElement.tag
            # print tableElement.text_content()
            print tableElement.xpath("/tbody")


if __name__ == "__main__":
    start()

