import pandas as pd
import numpy as np
import xlrd
import openpyxl
import datetime as dt
df = pd.read_csv("zamowienia.csv",sep=";")
print(df.Sprzedawca.unique())
print(df.Utarg.nlargest(5))
print("Kowalski wykonal",df.Sprzedawca[df.Sprzedawca=="Kowalski"].count(),"zamowiena")
print("Sowinski wykonal",df.Sprzedawca[df.Sprzedawca=="Sowiński"].count(),"zamowiena")
print("Peacock wykonal",df.Sprzedawca[df.Sprzedawca=="Peacock"].count(),"zamowiena")
print("Leverling wykonal",df.Sprzedawca[df.Sprzedawca=="Leverling"].count(),"zamowiena")
print("Dudek wykonal",df.Sprzedawca[df.Sprzedawca=="Dudek"].count(),"zamowiena")
print("Davolio wykonal",df.Sprzedawca[df.Sprzedawca=="Davolio"].count(),"zamowiena")
print("Callahan wykonal",df.Sprzedawca[df.Sprzedawca=="Callahan"].count(),"zamowiena")
print("Fuller wykonal",df.Sprzedawca[df.Sprzedawca=="Fuller"].count(),"zamowiena")
print("King wykonal",df.Sprzedawca[df.Sprzedawca=="King"].count(),"zamowiena")
kraje=df.Kraj.unique()
for x in kraje:
    print(x)
    print(df.Utarg[df.Kraj==x].sum())
df["Data zamowienia"]=pd.to_datetime(df["Data zamowienia"])
rok2005=df[df["Data zamowienia"].dt.year==2005]
print(rok2005[rok2005.Kraj=="Polska"])                                           #OPERACJE NA DATACH
rok2004=df[df["Data zamowienia"].dt.year==2004]
print(rok2004.Utarg.mean())
rok2005.to_csv("Zamowienia_2005.csv")
rok2004.to_csv("Zamowienia_2004.csv")