import pandas as pd
import numpy as np
import xlrd
import openpyxl
import datetime as dt
import matplotlib.pyplot as plt
df = pd.read_csv("iris.csv",sep=",")
print(len(df["sepal width"]))
data={  'a':df["sepal lenght"],
        'b':df["sepal width"],
        "c": np.random.randint(0,len(df["sepal width"],1),
        "d": np.random.randn(len(df["sepal width"]))}
# data['b'] = data['a'] + 10 * np.random.randn(150)
# data['d'] = np.abs(data['d']) * 100
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('wartość a')
# plt.ylabel('wartość b')
# plt.show()