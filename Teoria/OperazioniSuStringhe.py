#In questo eserizio vogliamo esplorare le proprietà delle stringhe
#len(): restituisce la lunghezza di una stringa(considera anche lo spazio vuoto)

stringa = "ciao amico"
print("la lunghezza della stringa e'? " + str(len(stringa)))

#upper(): converte la stringa in maiuscolo

stringa = "pagliaccio impiccati"
print(stringa.upper())

#lower(): converte in minuscolo una stringa

stringa = "FRATE COME STAI ?"
print(stringa.lower()); 

#capitalize(): solo la prima lettera in maiuscolo

stringa = "stefano"
print(stringa.capitalize())

#title(): ogni parola inizia con la Maiuscola

stringa = "la vendetta dei napoletani volanti 4"
print(stringa.title())

#swapcase(): caretteri in maiuscolo in minuscolo e viceversa

stringa = "PaLlOnE" 
print(stringa.swapcase())

#Esercizio si vuole scrivere una stringa in verticale

stringa  = input("inserisci una parola: ")

for i in range (int(len(stringa))):  
    print(stringa[i]) #Permette di stampare solo un carattere nella posizione i

