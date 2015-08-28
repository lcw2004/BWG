#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sqlite3

zidian_db_path = "bwg.db"


class BWGProductDao:

    def __init__(self):
        self.connect = sqlite3.connect(zidian_db_path)


    # 保存产品
    def save(self, product):
        sql = '''
            INSERT INTO Product ("prudoctName", "canOrder", "RAM", "HDD", "CPU", "BW", "Cost_Monthly", "Cost_Quarterly", "Cost_Half_Year", "Cost_Year")
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            '''

        cursor = self.connect.cursor()
        cursor.execute(sql, [product["prudoctName"],
                             product["canOrder"],
                             product["RAM"],
                             product["HDD"],
                             product["CPU"],
                             product["BW"],
                             product["Cost_Monthly"],
                             product["Cost_Quarterly"],
                             product["Cost_Half_Year"],
                             product["Cost_Year"]])
        cursor.close()
        self.connect.commit()


    # 修改产品
    def update(self, product):
        sql = '''
            UPDATE Product set canOrder=?, RAM=?, HDD=?, CPU=?, BW=?, Cost_Monthly=?, Cost_Quarterly=?, Cost_Half_Year=?, Cost_Year=?
            WHERE prudoctName = ?
            '''

        cursor = self.connect.cursor()
        cursor.execute(sql, [product["canOrder"],
                             product["RAM"],
                             product["HDD"],
                             product["CPU"],
                             product["BW"],
                             product["Cost_Monthly"],
                             product["Cost_Quarterly"],
                             product["Cost_Half_Year"],
                             product["Cost_Year"],
                             product["prudoctName"]])
        cursor.close()
        self.connect.commit()


    # 根据产品名称查询
    def get(self, productName):
        sql = 'SELECT prudoctName, canOrder, RAM, HDD, CPU, BW, Cost_Monthly, Cost_Quarterly, Cost_Half_Year, Cost_Year FROM Product WHERE prudoctName = ?'
        cursor = self.connect.cursor()
        cursor.execute(sql, [productName])

        one = cursor.fetchone()
        product = {}
        if one:
            product["prudoctName"] = one[0]
            product["canOrder"] = one[1]
            product["RAM"] = one[2]
            product["HDD"] = one[3]
            product["CPU"] = one[4]
            product["BW"] = one[5]
            product["Cost_Monthly"] = one[6]
            product["Cost_Quarterly"] = one[7]
            product["Cost_Half_Year"] = one[8]
            product["Cost_Year"] = one[9]
        cursor.close()
        return product


    # 根据产品名称检查是否能预订
    def canOrder(self, productName):
        product = self.get(productName)
        return product["canOrder"] == "1"


    # 根据产品名称检查是否存在
    def exicts(self, productName):
        sql = 'SELECT count(*)  FROM Product WHERE prudoctName = ?'
        cursor = self.connect.cursor()
        cursor.execute(sql, [productName])
        count = cursor.fetchone()[0]
        cursor.close()
        return count > 0


    # 获取所有能预订的列表
    def query(self, canOrder):
        sql = 'SELECT prudoctName, canOrder, RAM, HDD, CPU, BW, Cost_Monthly, Cost_Quarterly, Cost_Half_Year, Cost_Year FROM Product WHERE canOrder = ?'
        cursor = self.connect.cursor()
        cursor.execute(sql, [canOrder])

        all = cursor.fetchall()

        products = {}
        for one in all:
            product = {}
            product["prudoctName"] = one[0]
            product["canOrder"] = one[1]
            product["RAM"] = one[2]
            product["HDD"] = one[3]
            product["CPU"] = one[4]
            product["BW"] = one[5]
            product["Cost_Monthly"] = one[6]
            product["Cost_Quarterly"] = one[7]
            product["Cost_Half_Year"] = one[8]
            product["Cost_Year"] = one[9]
            products[one[0]] = product
        cursor.close()
        return products