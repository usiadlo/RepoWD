import pandas as pd
import numpy as np
import xlrd
import openpyxl
import datetime as dt
import matplotlib.pyplot as plt

x = np.arange(1,21,1)

plt.plot(x,1/x, '>g:',label="F(X)")
plt.axis([0, len(x),0,1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Wykres funkcji f(x)=1/x")
plt.legend()
plt.show()