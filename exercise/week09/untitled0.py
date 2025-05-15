#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 12 12:47:48 2025

@author: chaemin
"""

import sklearn
dir(sklearn)
dir(sklearn.linear_model)
dir(sklearn.linear_model.LinearRegression())
dir(sklearn.metrics)
dir(sklearn.metrics.r2_score)
help(sklearn.metrics.r2_score)

from sklearn.metrics import r2_score
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
r2_score(y_true, y_pred)