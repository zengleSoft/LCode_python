#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/6/16


import urllib.request
f=urllib.request.urlopen('http://119.97.201.28:6081/ShowPrice.aspx?gid=E010CC77-3D85-4483-A5C5-CE6242F8F97C&ch=w6XPUBQ5AI30MgBxd9jhMg==')
response=f.read()
print(str(response))
print(f.geturl())
print(f.read().decode('utf-8'))