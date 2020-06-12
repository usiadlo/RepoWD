with open("linijki.txt", "w+") as plik:
    plik.writelines("Linijka 1 \nLinijka 2 \nlinijka 3 \n")
    plik.seek(0,0)
    linia=plik.readlines()
    print(linia, end="")
    


