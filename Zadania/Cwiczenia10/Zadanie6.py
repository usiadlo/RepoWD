import pandas as pd
import numpy as np
import xlrd
import openpyxl
import datetime as dt
import matplotlib.pyplot as plt

xlsx=pd.ExcelFile('imiona.xlsx')
df=pd.read_excel(xlsx)
wbsa=df.Liczba[df["Plec"]=="K"].sum()
wba=df[df["Plec"]=="K"]
mbsa=df.Liczba[df["Plec"]=="M"].sum()
mba=df[df["Plec"]=="M"]
tag1=["Mezczyzni","Kobiety"]
w1=[mbsa,wbsa]



wby=np.array([])
for x in range(2000,2018):
    arr=wba.Liczba[wba["Rok"]==x].sum()          ##PETLA DO PETLI!!! WAZNE BARDZO!~!!!
    wby=np.append(wby,arr)


ywb=np.array([])
for x in range(2000,2018):
    ywb=np.append(ywb,x)


mby=np.array([])
for x in range(2000,2018):
    arr=mba.Liczba[mba["Rok"]==x].sum()          ##PETLA DO PETLI!!! WAZNE BARDZO!~!!!
    mby=np.append(mby,arr)


ymb=np.array([])
for x in range(2000,2018):
    ymb=np.append(ymb,x)

aba=np.array([])
for x in range(2000,2018):
    arr=df.Liczba[df["Rok"]==x].sum()          ##PETLA DO PETLI!!! WAZNE BARDZO!~!!!
    print(arr)
    aby=np.append(aba,arr)



plt.subplot(3,2,1)
plt.plot(ywb,wby)
plt.plot(ymb,mby)
plt.subplot(3,2,4)
plt.bar(tag1, w1)
plt.subplot(3,2,5)
plt.bar(ymb, aby)
plt.axis([2000, 2017, 0, 450000])



plt.show()