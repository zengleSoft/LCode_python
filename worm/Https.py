#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/7/9




def sendPostJson(url,paramentDict):
    import requests
    headers={'Content-Type':'application/json'}
    r = requests.post(url,json=paramentDict,headers=headers)
    print(r.raise_for_status())
    print(r.text)

def sendPostJson2(url,paramentDict):
    from urllib import request
    import json
    import socket
    headers = {
        'Content-Type': 'application/json'
    }
    socket.setdefaulttimeout(60)
    data = json.dumps(paramentDict).encode(encoding="utf-8")
    req = request.Request(url, headers=headers, data=data)
    res = request.urlopen(req).read()
    print(res)



if __name__ == '__main__':
    from _datetime import datetime
    s = '2018-07-10 16:16'
    i = 1500362356583
    local_str_time = datetime.utcfromtimestamp(i / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
    local_str_time2 = datetime.fromtimestamp(i / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
    print(local_str_time)
    print(local_str_time2)

