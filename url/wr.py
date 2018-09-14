#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 23:00
# @Author  : yangyuanqiang
# @File    : wr.py


fo = open("1.txt", "r+")
print("文件名: ", fo.name)

str = "6.www.runoob.com\r"
#在文件末尾写入一行
fo.seek(0, 2)
line = fo.write(str)