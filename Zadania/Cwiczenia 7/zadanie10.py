import numpy as np
m=np.arange(81).reshape(9,9)
for x in range(1,82):
    for y in range(1,82):
        if x*y==81:
            print(m.reshape(x,y))

print("Liczba mozliwosci wynosi tyle ile mozna utworzyc par x,y gdzie x*y = 81 poniewaz tyle wynosi liczba danych naszej macierzy")
