#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 22:29
# @Author  : yangyuanqiang
# @File    : wanip.py




import requests
import re

def get_ip_by_ip138():
    response = requests.get("http://2017.ip138.com/ic.asp")
    ip = re.search(r"\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\]",response.content.decode(errors='ignore')).group(0)
    return ip

# print("本机的ip地址为:",get_ip_by_ip138())
fo = open("ip.txt", "r+")

# str = "本机的ip地址为: ",get_ip_by_ip138()
#在文件末尾写入一行
fo.seek(0, 2)
line = fo.write("本机的ip地址为: " + get_ip_by_ip138() + "\r")