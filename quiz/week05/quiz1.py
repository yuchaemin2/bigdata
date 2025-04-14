#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 19:07:27 2025

@author: chaemin
"""

import csv
import matplotlib.pyplot as plt

def read_subway_data(filename):
    f = open(filename)
    data = csv.reader(f)
    next(data)  # 헤더 스킵
    next(data)
    s_in = [0] * 24
    s_out = [0] * 24
    for row in data:
        row[4:] = map(int, row[4:])
        for i in range(24):
            s_in[i] += row[4 + i * 2]     # 승차 인원
            s_out[i] += row[5 + i * 2]    # 하차 인원
    f.close()
    return s_in, s_out

# 각각의 CSV 파일에서 데이터 읽기
s_in_2018, s_out_2018 = read_subway_data('201803.csv')
s_in_2020, s_out_2020 = read_subway_data('202003.csv')
s_in_2025, s_out_2025 = read_subway_data('202503.csv')

# 그래프 그리기
plt.figure(dpi=300)
plt.rc('font', family='AppleGothic')
plt.title('지하철 시간대별 승하차 인원 추이(단위 1000만명)')

plt.plot(s_in_2018, label='201803승차', linestyle='-', color='blue')
plt.plot(s_out_2018, label='201803하차', linestyle=':', color='orange')

plt.plot(s_in_2020, label='202003승차', linestyle='-', color='green')
plt.plot(s_out_2020, label='202003하차', linestyle=':', color='red')

plt.plot(s_in_2025, label='202503승차', linestyle='-', color='purple')
plt.plot(s_out_2025, label='202503하차', linestyle=':', color='brown')

plt.legend()
plt.xticks(range(24), range(4, 28))  # 4시 ~ 27시로 표시
plt.show()
