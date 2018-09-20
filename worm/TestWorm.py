#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/6/16
import urllib
from urllib import request
from bs4 import BeautifulSoup



if __name__ == "__main__":
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
    # url = "http://www.whfg.gov.cn/zz_spfxmcx_fang.jspx?dengJh=%E5%A4%8F1700191&houseDengJh=%E5%A4%8F0006026"
    url = "http://119.97.201.28:6081/chktest2.aspx?gid=E010CC77-3D85-4483-A5C5-CE6242F8F97C"
    data1 = request.Request(url,headers=headers)
    data = urllib.request.urlopen(data1).read().decode("utf-8")

    print(data)