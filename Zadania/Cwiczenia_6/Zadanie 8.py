import numpy as np

def dziel(tab,kierunek):
    if kierunek=="pion":
        if tab.shape[1]%2==0:
            x=int(tab.shape[1]/2)
            print(tab[...,x:])
        else:
            print("zły wymiar tablicy")
    if kierunek=="poziom":
        if tab.shape[0]%2==0:
            x=int(tab.shape[0]/2)
            print(tab[x:])
        else:
            print("Zły wymiar tablicy")
    


        

a=np.array([[3,2,1],[2,3,7],[9,4,2],[2,10,7]])
dziel(a,"poziom")