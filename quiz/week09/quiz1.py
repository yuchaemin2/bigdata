#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 16:45:24 2025

@author: chaemin
"""

from sklearn.linear_model import LinearRegression
import numpy as np

# 데이터 정의
X = np.array([59, 49, 75, 54, 78, 56, 60, 82, 69, 83, 88, 94, 47, 65, 89, 70]).reshape(-1, 1)
Y = np.array([209, 180, 195, 192, 215, 197, 208, 189, 213, 201, 214, 212, 205, 186, 200, 204])

# 회귀 모델 학습
model = LinearRegression()
model.fit(X, Y)

# 회귀계수와 절편
alpha = model.intercept_  # 절편 α
beta = model.coef_[0]     # 기울기 β

# R_squared 값
r_squared = model.score(X, Y)

# X=58일 때 Y 예측
X_predict = np.array([[58]])
Y_predict = model.predict(X_predict)[0]

# 결과 출력
print(f"회귀식: Y = {alpha:.2f} + {beta:.2f} * X")
print(f"R-squared: {r_squared:.4f}")
print(f"X=58일 때 Y 예측값: {Y_predict:.2f}")
