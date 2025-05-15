#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 16:47:37 2025

@author: chaemin
"""

'''
from sklearn import linear_model
from sklearn import datasets
from sklearn.metrics import mean_squared_error
import pandas as pd

diabetes_data = datasets.load_diabetes()
X = pd.DataFrame(diabetes_data.data)
y = diabetes_data.target

linear_regression = linear_model.LinearRegression()
linear_regression.fit(X = pd.DataFrame(X), y = y)
prediction = linear_regression.predict(X = pd.DataFrame(X))
print('a value = ', linear_regression.intercept_)
print('b balue =', linear_regression.coef_)
residuals = y-prediction
SSE = (residuals**2).sum(); SST = ((y-y.mean())**2).sum()
R_squared = 1 - (SSE/SST)
print('R_squared = ', R_squared)
print('score = ', linear_regression.score(X = pd.DataFrame(X), y = y))
print('Mean_Squared_Error = ', mean_squared_error(prediction, y))
print('RMSE = ', mean_squared_error(prediction, y)**0.5)
'''

from sklearn import linear_model, datasets
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# 데이터 불러오기
diabetes_data = datasets.load_diabetes()
X = pd.DataFrame(diabetes_data.data, columns=diabetes_data.feature_names)
y = diabetes_data.target

# (1) 데이터 정보 출력
n_samples, n_features = X.shape
print(f"데이터 샘플 수: {n_samples}")
print(f"속성 수: {n_features}")
print("속성 이름:", diabetes_data.feature_names)

# (2) train/test 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 회귀 분석 수행
linear_regression = linear_model.LinearRegression()
linear_regression.fit(X_train, y_train)
y_pred = linear_regression.predict(X_test)

# 회귀 계수
a_value = linear_regression.intercept_
b_values = linear_regression.coef_

# 성능 평가
r_squared = linear_regression.score(X_test, y_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# 결과 출력
print("\n회귀 분석 결과")
print(f"절편 a = {a_value:.2f}")
print(f"회귀 계수 b = {b_values}")
print(f"R-squared = {r_squared:.4f}")
print(f"Mean Squared Error (MSE) = {mse:.2f}")
print(f"Root Mean Squared Error (RMSE) = {rmse:.2f}")
