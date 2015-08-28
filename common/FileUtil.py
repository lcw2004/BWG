#!/usr/bin/python
# -*- coding: UTF-8 -*-

def saveAsTemp(content, path):
    f = open(path, 'w')
    f.write(content)
    f.close()

def readFromFile(path):
    f = open(path, 'r')
    return f.read()