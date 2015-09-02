#!/usr/bin/python
# -*- coding: UTF-8 -*-

from BWG_DB import BWGProductDao
import BWG_Spider
from common import Config
from common.Mail import Email_Test_Sender
from common import HtmlUtil
import time


if __name__ == "__main__":

    count = 1
    while(True):
        print "--------------------------------"
        print "第 {0} 次爬取数据".format(count)
        pruductList = BWG_Spider.getProductListFromHomePage()

        # 保存数据库到数据库
        bwgProductDao = BWGProductDao()
        for key in pruductList:
            if bwgProductDao.exicts(key):
                bwgProductDao.update(pruductList[key])
            else:
                bwgProductDao.save(pruductList[key])

        # 检查是否能预订，如果能预订加入到可预订列表
        bwgProductDao = BWGProductDao()
        wantList = {}
        for pName in Config.PRODUCTS_WANT_ORDER:
            if bwgProductDao.canOrder(pName):
                wantList[pName] = bwgProductDao.get(pName)

                print "\tCan order：" + pName

        if len(wantList) > 0:
            # 构建邮件
            text = HtmlUtil.getMailHtml(wantList)

            # 发送邮件
            mailSender = Email_Test_Sender(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
            mailSender.sendMsg(Config.MAIL_USERNAME, "Bandwagonhost", text)

        count = count + 1
        time.sleep(Config.SPACE_TIME)
