#!/usr/bin/env python
# coding: utf-8

# In[1]:
# unit14 numpy 내용 - numpy 제거하고 실행해봄.
# age 파일 다루기 - 행정구역별 연령별 인구수
import csv   
f =open('age.csv', encoding='cp949')   # 행정구역, 총인구수, 연령구간인구수, 0세, 1세, 2세, ...
data = csv.reader(f)
next(data)  # 헤더 제거
for row in data :
    print(row)


# In[2]:
import csv
f =open('age.csv', encoding='cp949')
data = csv.reader(f)
next(data)
home = []  #입력 받은 지역의 데이터를 저장할 리스트 생성
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0] : #입력 받은 지역의 이름이 포함된 행 찾기
        areaname=row[0]
        for i in row[3:] : #3번 인덱스 값부터 슬라이싱 0세~
            home.append(int(i)) #입력 받은 지역의 데이터를 home에 저장
print(areaname, home) #home에 저장된 데이터 출력, areaname이 여러개일수있다...


# In[2]:
# 이제부터 numpy 사용 -> 제거
#import numpy as np
import csv
f =open('age.csv', encoding='cp949')
data = csv.reader(f)
next(data)
home = []  #입력 받은 지역의 데이터를 저장할 리스트 생성
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0] : #입력 받은 지역의 이름이 포함된 행 찾기
        areaname=row[0]
        for i in row[3:] : #3번 인덱스 값부터 슬라이싱 0세~
            home.append(int(i)) #입력 받은 지역의 데이터를 home에 저장

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize = (10,5), dpi=300)    
plt.rc('font', family ='AppleGothic')
plt.title(name +' 지역의 인구 구조')
plt.plot(home) 
plt.show()


# In[6]:
#import numpy as np
import csv
f =open('age.csv', encoding='cp949')
data = csv.reader(f)
next(data)
home = []  #입력 받은 지역의 데이터를 저장할 리스트 생성
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0] : #입력 받은 지역의 이름이 포함된 행 찾기
        areaname=row[0]
        for i in row[3:] : #3번 인덱스 값부터 슬라이싱 0세~
            home.append(int(i)) #입력 받은 지역의 데이터를 home에 저장

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize = (10,5), dpi=300)    
plt.rc('font', family ='AppleGothic')
plt.title(areaname +' 지역의 인구 구조')
plt.plot(home) 
plt.show()


# In[22]:
# 특정 지역의 연령별 인구와 다른 지역의 연령별 인구 비교 준비
#import numpy as np
import csv
f =open('age.csv', encoding='cp949')
data = csv.reader(f)
next(data)
# data=list(data)
home = []  #입력 받은 지역의 데이터를 저장할 리스트 생성
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0]: #입력 받은 지역의 이름이 포함된 행 찾기
        areaname=row[0]
        for i in row[3:]: #3번 인덱스 값부터 슬라이싱 0세~
            home.append(int(i)) #입력 받은 지역의 데이터를 home에 저장
        hometotal=int(row[2])
for k in range(len(home)):
    home[k]=(home[k]/hometotal) # 인구비율

for row in data : 
    away=[]
    for i in row[3:]: #3번 인덱스 값부터 슬라이싱 0세~
        away.append(int(i)) #입력 받은 지역의 데이터를 away에 저장
    awaytotal=int(row[2])
    for k in range(len(away)):
        away[k]=(away[k]/awaytotal)

    sum=0
    for j in range(len(away)):
        sum=sum+(home[j]-away[j])
    print(row[0], sum)


# In[29]:
import numpy as np
import csv
f = open('age.csv', encoding='cp949')
data = csv.reader(f)
next(data)
data = list(data)

name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn = 1 # 최솟값을 저장할 변수 생성 및 초기화
result_name = '' # 최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
result = 0 # 최솟값을 갖는 지역의 연령대별 인구 비율을 저장할 배열 생성 및 초기화
home = []  #입력 받은 지역의 데이터를 저장할 리스트 생성
for row in data :
    if name in row[0]: #입력 받은 지역의 이름이 포함된 행 찾기
        areaname=row[0]
        for i in row[3:]: #3번 인덱스 값부터 슬라이싱 0세~
            home.append(int(i)) #입력 받은 지역의 데이터를 home에 저장
        hometotal=int(row[2])
for k in range(len(home)):
    home[k]=(home[k]/hometotal) # ➊

for row in data : 
    away=[]
    for i in row[3:]: #3번 인덱스 값부터 슬라이싱 0세~
        away.append(int(i)) #입력 받은 지역의 데이터를 away에 저장
    awaytotal=int(row[2])
    for k in range(len(away)):
        away[k]=(away[k]/awaytotal)
    #print(row[0],away)
    sum=0
    for j in range(len(away)):
        sum=sum+(home[j]-away[j])
    #print(row[0], sum)
    if sum < mn : # ➍
        mn = sum # ➎
        result_name = row[0]
        result = away

print(result_name)
import matplotlib.pyplot as plt
plt.plot(home)
plt.plot(result)
plt.show()
# 결과가 이상...


# In[34]:
import numpy as np
import csv
#1. 데이터를 읽어온다.
f = open('age.csv', encoding='cp949')
data = csv.reader(f)
next(data)
data = list(data)
#2. 궁금한 지역의 이름을 입력받는다.
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn = 1 # 최솟값을 저장할 변수 생성 및 초기화
result_name = '' # 최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
result = 0 # 최솟값을 갖는 지역의 연령대별 인구 비율을 저장할 배열 생성 및 초기화
home = []  #입력 받은 지역의 데이터를 저장할 리스트 생성
#3. 궁금한 지역의 인구 구조를 저장한다.
for row in data :
    if name in row[0]: #입력 받은 지역의 이름이 포함된 행 찾기
        areaname=row[0]
        for i in row[3:]: #3번 인덱스 값부터 슬라이싱 0세~
            home.append(int(i)) #입력 받은 지역의 데이터를 home에 저장
        hometotal=int(row[2])
for k in range(len(home)):
    home[k]=(home[k]/hometotal) # ➊
#4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
for row in data : 
    away=[]
    for i in row[3:]: #3번 인덱스 값부터 슬라이싱 0세~
        away.append(int(i)) #입력 받은 지역의 데이터를 away에 저장
    awaytotal=int(row[2])
    for k in range(len(away)):
        away[k]=(away[k]/awaytotal)
    #print(row[0],away)
    sum=0
    for j in range(len(away)):
        sum=sum+(home[j]-away[j])**2 #    s = np.sum((home - away) **2)
    #print(row[0], sum)
    if sum < mn and name not in row[0] : # ➍
        mn = sum # ➎
        result_name = row[0]
        result = away
#5. 궁금한 지역의 인구 구조와 가장 비슷한 곳의 인구 구조를 시각화한다.
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize = (10,5), dpi=300)            
plt.rc('font', family ='AppleGothic')
plt.title(name +' 지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home, label = name)
plt.plot(result, label = result_name)
plt.legend()
plt.show()


# In[44]:
import numpy as np
import csv
#1. 데이터를 읽어온다.
f = open('age.csv', encoding='cp949')
data = csv.reader(f)
next(data)
data = list(data)
#2. 궁금한 지역의 이름을 입력받는다.
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn = 1 # 최솟값을 저장할 변수 생성 및 초기화
result_name = '' # 최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
result = 0 # 최솟값을 갖는 지역의 연령대별 인구 비율을 저장할 배열 생성 및 초기화
home = []  #입력 받은 지역의 데이터를 저장할 리스트 생성
#3. 궁금한 지역의 인구 구조를 저장한다.
for row in data :
    if name in row[0]: #입력 받은 지역의 이름이 포함된 행 찾기
        areaname=row[0]
        for i in row[3:]: #3번 인덱스 값부터 슬라이싱 0세~
            home.append(int(i)) #입력 받은 지역의 데이터를 home에 저장
        hometotal=int(row[2])
for k in range(len(home)):
    home[k]=(home[k]/hometotal) # ➊
#4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
result_list=[]
for row in data : 
    away=[]
    for i in row[3:]: #3번 인덱스 값부터 슬라이싱 0세~
        away.append(int(i)) #입력 받은 지역의 데이터를 away에 저장
    awaytotal=int(row[2])
    for k in range(len(away)):
        away[k]=(away[k]/awaytotal)
    s=0
    for j in range(len(away)):
        s=s+(home[j]-away[j])**2
    result_list.append([row[0], away, s])
result_list.sort(key=lambda s: s[2]) # sum 값으로 정렬...

#5. 궁금한 지역의 인구 구조와 가장 비슷한 곳의 인구 구조를 시각화한다.
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize = (10,5), dpi=300)            
plt.rc('font', family ='AppleGothic')
plt.title(name +' 지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home, label = name)
for i in range(10):
    plt.plot(result_list[i+1][1], label = result_list[i+1][0])

plt.legend()
plt.show()


# In[ ]:




