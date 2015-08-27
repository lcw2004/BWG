#!/usr/bin/python
# -*- coding: UTF-8 -*-

import BWG_Spider
from BWG_DB import BWGProductDao

if __name__ == "__main__":
    pruductList = BWG_Spider.getProductListFromHomePage()
    for key in pruductList:
        bwgProductDao = BWGProductDao()
        if bwgProductDao.exicts("Bandwagon 960G - PROMO"):
            bwgProductDao.update(pruductList[key])
        else:
            bwgProductDao.save(pruductList[key])


