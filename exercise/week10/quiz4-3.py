#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 16:20:52 2025

@author: chaemin
"""
'''

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the iris dataset
iris = load_iris()
x = iris.data
y = iris.target
target_names = iris.target_names

# Split into train and test
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train the classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, Y_train)

# New sample to predict
sample = [[5.6, 2.9, 3.6, 1.3]]

# Predict
predicted_class = clf.predict(sample)[0]
predicted_label = target_names[predicted_class]

print("예측된 품종:", predicted_label)
'''
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# 데이터셋 로드
iris = load_iris()
X = iris.data
y = iris.target

# 모델 학습
rfc = RandomForestClassifier(n_estimators=100, random_state=42)
rfc.fit(X, y)

# 테스트할 샘플
myX_test = np.array([[5.6, 2.9, 3.6, 1.3]])

# 예측
myprediction = rfc.predict(myX_test)
print("예측된 클래스 번호:", myprediction[0])
print("예측된 품종:", iris.target_names[myprediction[0]])

from sklearn.tree import export_graphviz
import graphviz

# 첫 번째 트리 선택
estimator = rfc.estimators_[0]

# dot 파일로 export
dot_data = export_graphviz(estimator,
                           out_file=None,
                           feature_names=iris.feature_names,
                           class_names=iris.target_names,
                           rounded=True,
                           filled=True)

# Graphviz로 시각화
graph = graphviz.Source(dot_data)
graph.render("iris_tree", format="png", cleanup=True)
graph  # Jupyter Notebook에서는 이 라인으로 시각화됨


from sklearn.tree import _tree

tree = estimator.tree_
feature_names = iris.feature_names

def print_decision_path(input_sample):
    node = 0  # root
    while tree.children_left[node] != _tree.TREE_LEAF:
        feature = tree.feature[node]
        threshold = tree.threshold[node]
        print(f"Node {node}: if {feature_names[feature]} <= {threshold:.2f}")
        if input_sample[0][feature] <= threshold:
            node = tree.children_left[node]
        else:
            print(f"Node {node}: else go right")
            node = tree.children_right[node]
    print(f"→ 최종 리프 노드 {node}, 클래스 예측: {iris.target_names[np.argmax(tree.value[node])]}")


print_decision_path(myX_test)
