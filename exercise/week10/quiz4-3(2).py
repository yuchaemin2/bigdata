#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 16:24:49 2025

@author: chaemin
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_graphviz
import graphviz

# 1. 데이터 불러오기
iris = load_iris()
X = iris.data
y = iris.target

# 2. 모델 학습
rfc = RandomForestClassifier(n_estimators=100, random_state=42)
rfc.fit(X, y)

# 3. 예측할 샘플
myX_test = np.array([[5.6, 2.9, 3.6, 1.3]])
myprediction = rfc.predict(myX_test)
print("예측된 클래스 번호:", myprediction[0])
print("예측된 품종:", iris.target_names[myprediction[0]])

# 4. 결정 트리 중 하나를 시각화
estimator = rfc.estimators_[0]  # 첫 번째 트리 선택

dot_data = export_graphviz(estimator,
                           out_file=None,
                           feature_names=iris.feature_names,
                           class_names=iris.target_names,
                           rounded=True,
                           filled=True)

# 5. Jupyter Notebook에서 직접 출력
graph = graphviz.Source(dot_data)
graph  # 이 줄은 Jupyter에서 그래픽 출력됨
