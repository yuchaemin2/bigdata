# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd

## 질의 3-1
emp = pd.read_csv('emp.csv')

# 질의 3-2
print(emp)
emp
emp[:]
emp[:][:]

emp.loc[:]
emp.loc[:,:]

emp.iloc[:]
emp.iloc[:,:]


# 3-3

emp.ENAME # csv파일에 ENAME로 정의되어있음
emp['ENAME']
emp.loc[:, 'ENAME']
emp.loc[:]['ENAME']

# 3-4
emp[['ENAME', 'SAL']]
emp.loc[:,['ENAME', 'SAL']]
emp.iloc[:,[1,5]]

emp.loc[0:13,['ENAME', 'SAL']]
emp.iloc[0:13,['ENAME', 'SAL']] # xxx이렇게 하면 안됨
emp.iloc[0:14, [1,5]]

# 3-5
emp['JOB']
emp['JOB'].unique()
emp['JOB'].drop_duplicates() # 시리즈

# 3-6
emp[emp['SAL'] < 2000]

# 3-7
emp[(emp['SAL'] >= 1000) & (emp['SAL'] <= 2000)]

# 3-8
emp[(emp['SAL'] >= 1500) & (emp['JOB'] == 'SALESMAN')]

# 3-9
emp[emp['JOB'].isin(['MANAGER', 'CLERK'])]

# 3-10
emp[~emp['JOB'].isin(['MANAGER', 'CLERK'])]

# 3-11
emp[emp['ENAME'] == 'BLAKE'][['ENAME', 'JOB']]

# 3-12
emp[emp['ENAME'].str.contains('AR')][['ENAME', 'JOB']]

# 3-13
emp[(emp['ENAME'].str.contains('AR')) & (emp['SAL'] >= 2000)]

# 3-14
emp.sort_values(by='ENAME')

# 3-15
emp['SAL'].sum()

# 3-16
emp[emp['JOB'] == 'SALESMAN']['SAL'].sum()

# 3-17
emp['SAL'].agg(['sum', 'mean', 'min', 'max'])

# 3-18
emp.shape[0]

# 3-19
emp.groupby('JOB')['SAL'].agg(['count', 'sum'])

# 3-20
emp[emp['COMM'].notnull()]
