#!/usr/bin/python
# -*- coding: UTF-8 -*-

from mako.template import Template


def getMailHtml(wantList):
    mytemplate = Template(filename='common/Mail.html', input_encoding='utf-8', output_encoding='utf-8')
    return mytemplate.render(productList=wantList)
