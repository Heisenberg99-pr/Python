
#stapmpare un quadrato di asterischi di lato n
n = input("inserisci il lato del quadrato: ")
n = int(n); 
for i in range(n):
    print("*"*n)

#stampare un quadrato fatto di asterischi con lato n, vuoto

n = int(input("inserisci il lato del quadrato:"))
riga_piena = ("*"*n)
riga_vuota = ("*" + " "*(n-2) + "*")

print(riga_piena)
for i in range(n-2):
    print(riga_vuota)

print (riga_piena)
    



