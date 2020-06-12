import numpy as np
def wyraz(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return wyraz(n-1)+wyraz(n-2)
def fib():
    lista=np.array([wyraz(i) for i in range (0,25)])
    print(lista.reshape((5,5)))

fib()
