#!/usr/bin/python
# -*- coding: UTF-8 -*-

import BWG_Spider

if __name__ == "__main__":
    pruductList = BWG_Spider.getProductListFromHomePage()
    for key in pruductList:
        print key, pruductList[key]
