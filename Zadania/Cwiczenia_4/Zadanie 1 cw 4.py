lista=[x for x in range(100) if x%4==0]
liczby=open("Liczby.txt","w+")
liczby.write(str(lista))
liczby.close()