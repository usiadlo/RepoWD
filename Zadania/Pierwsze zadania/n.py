jeden=int(5)
dwa=int(2)
wyraz=str('Przybij ')
wyraz2=str('Dej ' + str(dwa)+ ' zlote')
com=complex(1+2j)
plex=complex(2-3j)
flo=float(2.1)
at=float(3.4)
print(wyraz,jeden,wyraz2)
print(com, plex)
print(flo,at)
                                                    ##ZADANIE 2 CW 1##
a=int(input('Podaj liczbe '))
znak=input('Podaj znak (+,-,*,/) ')
b=int(input('Podaj druga liczbe '))
if znak=='+':
    print(a+b)
if znak=='-':
    print(a-b)
if znak=='*':
    print(a*b)
if znak=='/':
    if b==0:
        print("Nie mozna dzielic przez zero!! NONONO")
    else:
        print(a/b)
                                                            ##ZADANIE 3 CW 1##
a=9
print("Liczba na ktorej wykonuje operacje to ", a)
a+=1
print("operator przyrostkowy '+' =" , a)
a-=1
print("operator przyrostkowy '-' =", a)
a/=3
print("operator przyrostkowy '/' =", a)
a*=2
print("operator przyrostkowy '*' =" , a)
a**=1
print("operator przyrostkowy '**' =" , a)
a%=1
print("operator przyrostkowy '%' =" , a)
                                                            ##ZADANIE 4 CW 1##
import math
print(exp(10))
print(pow(log(5+pow(sin(8),2)),(1/6)))
print("Wartosc bezwzgledna z 3,55 wynosi: ",fabs(3.55))
print("Wartosc bezwzgledna z 4,80 wynosi: ",fabs(4.80))
                                                            ##ZADANIE 5 CW 1##
imie="DAWID"
nazwisko="TERCJAK"
print(str.capitalize(imie ),str.capitalize(nazwisko))
                                                            ##ZADANIE 6 CW 1##

string=str("""Ore, ore
szabadabada amore .
Hej amore szabadabada.
O muriaty, szagariaty,
Hajda trojka na mienia .
Ore, ore
szabadabada amore .
Hej amore szabadabada.
O muriaty, szagariaty,
Hajda trojka na mienia.
Gdy śpiewamy,
słucha cała ziemia .
Gdy śpiewamy, słucha każdy rad.
Niechaj każdy z nami śpiewa.
Niech rozbrzmiewa piosnka ta .
Niechaj każdy z nami śpiewa.
Niech rozbrzmiewa piosnka ta.
Ore, ore
szabadabada amore ,
Hej amore szabadabada.
O muriaty, szagariaty,
Hajda trojka na mienia .
Ore, ore
szabadabada amore ,
Hej amore szabadabada.""")
amore="amore"
print(string.count(amore))
                                                            ##ZADANIE 7 CW 1##
JestDobrze='JeorkszireD'
print(JestDobrze[0],JestDobrze[10])
                                                            ##ZADANIE 8 CW 1##
string=("""Ore, ore
szabadabada amore ,
Hej amore szabadabada""")
print(string.split(" "))
                                                            ##ZADANIE 9 CW 1##

a=float(1)
b=str(3)
c=int(15)

print("To jest zmienna typu float: %f, to jest zmienna typu string: %s, a to jest zmienna typu szesnastkowego: %x" % (a,b,c))
                                                            ##ZADANIE 10 CW 1##
films=["Scooby-Doo","50 Twarzy Grey'a","Titanic","Diabeu ubiera sie u Prady"]
films.sort()
print(films)
                                                            ##ZADANIE 11 CW 1##
import math
import tabulate
angles=[0,30,45,60,90]
value_sin=[0,1/2,(sqrt(2))/2,(sqrt(3))/2,1,0]
value_cos=[1,]
value_tg=[0,]
value_ctg=["-",]
print(angles)
print(value_sin)
print(tabulate(angles))