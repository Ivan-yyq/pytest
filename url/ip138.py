#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 15:11
# @Author  : yangyuanqiang
# @File    : ip138.py


import requests
from bs4 import BeautifulSoup


# 获取外网IP
def get_out_ip(url):
    r = requests.get(url)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    print('本机的ip地址为: ' + ip)
    return ip


def get_real_url(url=r'http://www.ip138.com/'):
    r = requests.get(url)
    txt = r.text
    soup = BeautifulSoup(txt,"html.parser").iframe
    return soup["src"]

if __name__ == '__main__':
    get_out_ip(get_real_url())