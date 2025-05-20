#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 16:16:47 2025

@author: chaemin
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
x = iris.data
y = iris.target

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Different n_estimators to try
n_estimators_list = [1, 5, 10, 20, 50, 100, 150, 200, 250, 300]
accuracies = []

# Loop through n_estimators
for n in n_estimators_list:
    clf = RandomForestClassifier(n_estimators=n, random_state=42)
    clf.fit(X_train, Y_train)
    pred = clf.predict(X_test)
    acc = accuracy_score(Y_test, pred)
    accuracies.append(acc)
    print(f"n_estimators = {n}, Accuracy = {acc:.4f}")

plt.plot(n_estimators_list, accuracies, marker='o')
plt.title("Accuracy vs n_estimators")
plt.xlabel("n_estimators")
plt.ylabel("Accuracy")
plt.grid(True)
plt.show()
