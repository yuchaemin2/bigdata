#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 12:52:14 2025

@author: chaemin
"""

import pandas as pd

# 질의 4-0: emp.csv를 읽어서 DataFrame emp 만들기
emp = pd.read_csv('emp.csv')

# 질의 4-1: age 열 추가
emp['AGE'] = [30, 40, 50, 30, 40, 50, 30, 40, 50, 30, 40, 50, 30, 40]

# 질의 4-2: 새로운 행 추가
new_row = pd.DataFrame({'EMPNO': [9999], 'ENAME': ['ALLEN'], 'JOB': ['SALESMAN']})
emp = pd.concat([emp, new_row], ignore_index=True)

# 질의 4-3: ename='ALLEN' 행 삭제
emp = emp[emp['ENAME'] != 'ALLEN']

# 질의 4-4: hiredate 열 삭제
emp = emp.drop(columns=['HIREDATE'], errors='ignore')

# 질의 4-5: ename='SCOTT'의 sal을 3000으로 변경
emp.loc[emp['ENAME'] == 'SCOTT', 'SAL'] = 3000

# 질의 5-1: sal 컬럼을 oldsal로 이름 변경
emp = emp.rename(columns={'SAL': 'OLDSAL'})

# 질의 5-2: newsal 컬럼 추가 (oldsal 값 복사)
emp['NEWSAL'] = emp['OLDSAL']

# 질의 5-3: oldsal 컬럼 삭제
emp = emp.drop(columns=['OLDSAL'])

# 변경된 DataFrame 저장 (선택 사항)
# emp.to_csv('updated_emp.csv', index=False)
