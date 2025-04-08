#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 19:34:28 2025

@author: chaemin
"""

import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
df_2015 = pd.read_csv('201502.csv', encoding='cp949')
df_2025 = pd.read_csv('202502.csv', encoding='cp949')

print(df_2015.columns)

# 지역 기준으로 정렬 (그래프 비교가 쉬움)
df_2015 = df_2015.sort_values('Unnamed: 0')
df_2025 = df_2025.sort_values('Unnamed: 0')

# 인구 데이터 추출
regions = df_2015['Unnamed: 0'].values
pop_2015 = df_2015['Unnamed: 1'].values
pop_2025 = df_2025['Unnamed: 1'].values

# 바 너비 및 위치 설정
import numpy as np
x = np.arange(len(regions))
width = 0.35

# 그래프 그리기

plt.bar(x - width/2, pop_2015, width, label='2015년 2월')
plt.bar(x + width/2, pop_2025, width, label='2025년 2월')
plt.style.use('ggplot')
plt.figure(figsize = (10,5), dpi=300)    
plt.rc('font', family ='AppleGothic')
plt.show()

# 라벨, 제목, 범례
plt.xlabel('지역')
plt.ylabel('인구수')
plt.title('지역별 인구 변화 (2015년 vs 2025년)')
plt.xticks(x, regions, rotation=45)
plt.legend()
plt.tight_layout()

# 저장 및 출력
plt.savefig('population_change.png')
plt.show()
