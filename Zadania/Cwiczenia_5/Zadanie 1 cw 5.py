class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
    def wyswietl_nazwe(self):
        print([self.rodzaj])



class Ubrania(Material):
    rozmiar="XXL"
    kolor="Czarny"
    dla_kogo="Dla puszystych"
    def wyswietl_dane(self):
        print(self.rozmiar,self.kolor, self.dla_kogo, self.rodzaj, self.dlugosc,self.szerokosc)



class Sweter(Ubrania):
    rodzaj_swetra="Golf"
    def wyswietl_dane(self):
        print(self.rodzaj_swetra,self.rozmiar,self.kolor,self.dla_kogo)


mat=Material("Bawełna",10,20)
ubr=Ubrania("Jedwab",5,5)
swe=Sweter("Kaszmir",50,20)
swe.wyswietl_dane()
mat.wyswietl_nazwe()
