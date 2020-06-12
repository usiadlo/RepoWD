import pandas as pd
import numpy as np
import xlrd
import openpyxl
xlsx=pd.ExcelFile('imiona.xlsx')
df=pd.read_excel(xlsx)
rok=df.groupby(['Rok'])
for x in range(2000,2018):
    print(rok.get_group(x)[rok.get_group(x)["Liczba"]>1000])
print(df[df["Imie"]=="DAWID"])
print(df.Liczba.sum())
lata=df[((df.Rok >2000) & (df.Rok<2005))]
print(lata.Liczba.sum())
print(lata[lata["Plec"]=="M"].Liczba.sum())
print(lata[lata["Plec"]=="K"].Liczba.sum())
mez=df[df.Plec=="M"]
kob=df[df.Plec=="K"]
maxmez=mez.Liczba.max()
print(mez.Imie[mez.Liczba==maxmez],"All tajm faceci")
maxkob=kob.Liczba.max()
print(kob.Imie[kob.Liczba==maxkob],"All tajm kobiety")

for x in range(2000,2018):
    mezrok=mez[mez.Rok==x]
    maxmezrok=mezrok.Liczba.max()
    print(mezrok.Imie[mezrok.Liczba==maxmezrok],"Mezczyzna w roku ",x)
for x in range(2000,2018):
    kobrok=kob[kob.Rok==x]
    maxkobrok=kobrok.Liczba.max()
    print(kobrok.Imie[kobrok.Liczba==maxkobrok],"Kobieta w roku ",x)
