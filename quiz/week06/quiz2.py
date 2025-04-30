#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 14:04:43 2025

@author: chaemin
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# JSON 데이터를 DataFrame으로 변환
with open('/Users/chaemin/Documents/bigdata/exercise/week06-v2/china_visitors_2020_202502.json') as f:
    js = json.load(f)  # json.loads(f.read()) 도 되지만 json.load(f)로 간단히 가능

df = pd.DataFrame(js)  # 중복 선언 제거 (기존에 있던 "data"는 없어도 됨)

# yyyymm을 datetime 형식으로 바꿔서 정렬 (시각화 시 순서 문제 방지)
df['yyyymm'] = pd.to_datetime(df['yyyymm'], format='%Y%m')
df = df.sort_values('yyyymm')

# 그래프 그리기
plt.figure(figsize=(18, 6))  # 그래프 크기 조절
plt.bar(df['yyyymm'].dt.strftime('%Y-%m'), df['visit_cnt'], color='skyblue')

plt.title('Trend of Monthly Chinese Visitors to Korea (2020~2025)', fontsize=16)
plt.xlabel('Year-Month', fontsize=12)
plt.ylabel('Number of Visitors', fontsize=12)
plt.xticks(rotation=45, ha='right')  # x축 날짜 회전
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()