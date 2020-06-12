class Slowa:
    def __init__(self,slowo1,slowo2):
        self.slowo1=slowo1
        self.slowo2=slowo2
    def sprawdz_czy_palindrom(self):
        if self.slowo1==self.slowo1[::-1]:
            print("Słowo",self.slowo1,"jest palindromem")
        else:
            print("Słowo",self.slowo1,"nie jest palindromem")
        if self.slowo2==self.slowo2[::-1]:
            print("Słowo",self.slowo2,"jest palindromem")
        else:
            print("Słowo",self.slowo2,"nie jest palindromem")
    def sprawdz_czy_metagramy(self):
        n=len(self.slowo1)
        for x in range(0,n):
            if self.slowo1[x]==self.slowo2[x]:
                if x==n-1:
                    print("Slowa sa metagramami")
                    
    def sprawdz_czy_anagramy(self):
        n=len(self.slowo1)
        m=len(self.slowo2)
        z = 0
        x = 0
        while x<=m:
            while z<=n:
                if self.slowo1[x]==self.slowo2[z]:
                    print("jejegutuut")
                else:
                    print("hellno")
                z+=1
            x+=1




nowe=Slowa("tama","mata")
nowe.sprawdz_czy_palindrom()
nowe.sprawdz_czy_metagramy()
nowe.sprawdz_czy_anagramy()