import pandas as pd
import numpy as np
import xlrd
import openpyxl
import datetime as dt
import matplotlib.pyplot as plt

x=np.arange(0,31,0.1)
s=np.sin(x)
c=np.cos(x)
plt.title("Wykres f(x)")
plt.plot(x,s,label='sin(x)')
plt.plot(x,c,label="cos(x)")
plt.xlabel("x")
plt.xlabel("f(x)")
plt.legend()
plt.show()