import pandas as pd
import numpy as np
import xlrd
import openpyxl
import datetime as dt
import matplotlib.pyplot as plt

x=np.arange(0,31,0.1)
s=np.sin(x)+2
s2=np.sin(x+3)
plt.title("Wykres f(x)")
plt.plot(x,s,label='sin(x)')
plt.plot(x,s2,label="cos(x)")
plt.axis([-1, 30,-1,3])
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()