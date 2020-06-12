class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
    def wyswietl_produkt(self):
        print(self.nazwa_produktu,"w ilosci",self.ilosc, "szt.","w cenie", self.cena_jed, "zl",self.jednostka_miary)
    def ile_produktu(self):
        print(self.ilosc,self.jednostka_miary)
    def ile_kosztuje(self):
        print(self.cena_jed*self.ilosc,"zł")
    
Koszulka= NaZakupy("Tshirt",3,"szt.",2)
Koszulka.wyswietl_produkt()
Koszulka.ile_produktu()
Koszulka.ile_kosztuje()
