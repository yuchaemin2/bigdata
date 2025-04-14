#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 12:31:32 2025

@author: chaemin
"""

'''
# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
client_id = "w4lh9sZm30AN2eJmDSZ6"
client_secret = "OtPsjTJKA_"
encText = urllib.parse.quote("바이브 프로그래밍")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    myresult=response_body.decode('utf-8')
    print(myresult)
else:
    print("Error Code:" + rescode)
'''


import os
import sys
import urllib.request
client_id = "LBo2JT7AQn4mXtyb3EEB"
client_secret = "xXRoXIpERC"
encText = urllib.parse.quote("엔시티위시 재희")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    myresult = response_body.decode('utf-8')
    print(myresult)
else:
    print("Error Code:" + rescode)
