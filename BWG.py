#!/usr/bin/python
# -*- coding: UTF-8 -*-

from BWG_DB import BWGProductDao
import BWG_Spider
from common import Config
from common.Mail import Email_Test_Sender
from common import HtmlUtil

def build_text(wantList):
    text = "可预订产品如下：\n"
    for pName in wantList:
        product = wantList.get(pName)
        text += "<p>" + pName + "\n" + "</p><br>"
    return text

if __name__ == "__main__":
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

    # 构建邮件
    text = HtmlUtil.getMailHtml(wantList)
    print text

    # 发送邮件
    mailSender = Email_Test_Sender(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
    mailSender.sendMsg(Config.MAIL_TO_QQ, "搬瓦工优惠", text)




