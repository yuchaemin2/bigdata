#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 13:13:08 2025

@author: chaemin
"""

# Python3 샘플 코드 #

import requests

url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
params ={'serviceKey' : '2FK+LiX3igCZ0VGxui7olZjXXNYepuHjRnwO0lofDIg0RORmZmyHfuRkFYgdQXQzcrP0fJMEytwHLcx4ZEm+bw==', 'YM' : '201201', 'NAT_CD' : '112', 'ED_CD' : 'E' }

response = requests.get(url, params=params)
print(response.content)