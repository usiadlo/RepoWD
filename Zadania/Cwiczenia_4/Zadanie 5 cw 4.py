class Ciag:
    def __init__(self,a1,n,r):
        self.a1=a1
        self.n=n
        self.r=r
    def wyswietl_dane(self):
        print("Pierwszy wyraz wynosi",self.a1,"Liczba elementow wynosi",self.n,"Roznica wynosi",self.r)
    def pobierz_elementy(self):
        self.a4=int(input("Podaj czwarty wyraz ciagu "))
        self.a7=int(input("Podaj siódmy wyraz ciagu "))
        self.a3=int(input("Podaj trzeci wyraz ciagu "))
    def pobierz_parametry(self):
        self.a1=int(input("Podaj pierwszy wyraz ciagu "))
        self.r=int(input("Podaj roznice ciagu "))
        self.n=int(input("Podaj ilosc elementow ciagu "))
    def policz_sume(self):
        sn=((self.a1+(self.a1+(self.n-1)*self.r))/2)*self.n
        print(sn)
    def policz_elementy(self):
        for i in range(0,self.n):
            an=self.a1+(i-1)*self.r
            print(an)
    
            


Pierwszy= Ciag(1,5,3)
Pierwszy.wyswietl_dane()
Pierwszy.pobierz_elementy()
Pierwszy.pobierz_parametry()
Pierwszy.policz_sume()
Pierwszy.policz_elementy()