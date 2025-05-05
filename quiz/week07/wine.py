#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  2 22:54:20 2025

@author: chaemin
"""

import pandas as pd

red_df = pd.read_csv('DATA/winequality-red.csv', sep = ';', header = 0, engine = 'python')

white_df = pd.read_csv('DATA/winequality-white.csv', sep = ';', header = 0, engine= 'python')

red_df.to_csv('DATA/winequality-red2.csv', index = False)

white_df.to_csv('DATA/winequality-white2.csv', index = False)

# 4.2 데이터 병합하기 ------------------------------------------------------------
# 1. 레드 와인과 화이트 와인 파일 합치기
red_df.head()

red_df.insert(0, column = 'type', value = 'red')

red_df.head()

red_df.shape

white_df.head()

white_df.insert(0, column = 'type', value = 'white')

white_df.head()

white_df.shape

wine = pd.concat([red_df, white_df])

wine.shape

wine.to_csv('DATA/wine.csv', index = False)


#5 데이터 탐색 -----------------------------------------

#1. 기본 정보 확인하기
print(wine.info())

#2. 함수를 사용해 기술 통계 구하기
wine.columns = wine.columns.str.replace(' ', '_') #
wine.head()
wine.describe()
sorted(wine.quality.unique())
wine.quality.value_counts()


# 6 데이터 모델링 -----------------------------------

# 6.1 describe( ) 함수로 그룹 비교하기
wine.groupby('type')['quality'].describe()
wine.groupby('type')['quality'].mean()
wine.groupby('type')['quality'].std()
wine.groupby('type')['quality'].agg(['mean', 'std'])

# 6.2 t-검정과 회귀 분석으로 그룹 비교하기
### cmd창에서 통계패키지 설치하기:  pip install statsmodels 
from scipy import stats
from statsmodels.formula.api import ols, glm
red_wine_quality = wine.loc[wine['type'] == 'red', 'quality']
white_wine_quality = wine.loc[wine['type'] == 'white', 'quality']
stats.ttest_ind(red_wine_quality, white_wine_quality, equal_var = False)

Rformula = 'quality ~ fixed_acidity + volatile_acidity + citric_acid + residual_sugar + chlorides + free_sulfur_dioxide + total_sulfur_dioxide + density + pH + sulphates + alcohol'

regression_result = ols(Rformula, data = wine).fit()

regression_result.summary()

# 6.3 회귀 분석 모델로 새로운 샘플의 품질 등급 예측하기
sample1 = wine[wine.columns.difference(['quality', 'type'])]
sample1 = sample1[0:5][:]
sample1_predict = regression_result.predict(sample1)
sample1_predict
wine[0:5]['quality']

data = {"fixed_acidity" : [8.5, 8.1], "volatile_acidity":[0.8, 0.5],
"citric_acid":[0.3, 0.4], "residual_sugar":[6.1, 5.8], "chlorides":[0.055,
0.04], "free_sulfur_dioxide":[30.0, 31.0], "total_sulfur_dioxide":[98.0,
99], "density":[0.996, 0.91], "pH":[3.25, 3.01], "sulphates":[0.4, 0.35],
"alcohol":[9.0, 0.88]}

sample2 = pd.DataFrame(data, columns= sample1.columns)
sample2


sample2_predict = regression_result.predict(sample2)
sample2_predict


# 7 결과 시각화 --------------------------------------------
#7.1 와인 유형에 따른 품질 등급 히스토그램 그리기
###cmd 창에서 패키지 설치하기:   pip install seaborn 

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')

sns.histplot(red_wine_quality, stat='density', kde = True, color = "red", label = 'red wine')
sns.histplot(white_wine_quality, stat='density', kde = True, label = 'white wine')
plt.title("Quality of Wine Type")
plt.legend()
plt.show()


#7.2 부분 회귀 플롯으로 시각화하기
import statsmodels.api as sm
others = list(set(wine.columns).difference(set(["quality", "fixed_acidity"])))
p, resids = sm.graphics.plot_partregress("quality", "fixed_acidity", others, data = wine, ret_coords = True)
plt.show()

fig = plt.figure(figsize = (8, 13))
sm.graphics.plot_partregress_grid(regression_result, fig = fig)
plt.show()