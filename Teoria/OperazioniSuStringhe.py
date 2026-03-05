

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

#possiamo verificare la presenza di una frase o un carattere nella stringa, ad esempio:
stringa = "ciao amico"
print("ciao" in stringa) # restituisce True, perché "ciao" è nella stringa
print("mondo" in stringa) # restituisce False, perché "mondo" non è nella stringa

#Oppure al contrario:
stringa = "ciao amico"
print("ciao" not in stringa) # restituisce False, perché "ciao" è nella stringa
print("mondo" not in stringa) # restituisce True, perché "mondo" non è nella stringa

'''
Operazione di Slicing:
Permette di estrarre una parte della stringa, specificando
indice di inizioe e fine della parte da estrarre, esempi di opreazioni
di slicing:
'''
stringa = "Programmazione in Python!"
print(stringa[3:7]) # restituisce "gram", perché estrae i caratteri dalla posizione 3 alla posizione 6 (7-1)
print(stringa[:7]) # restituisce "Program", perché estrae i caratteri dalla posizione 0 alla posizione 6 (7-1)
print(stringa[3:]) # restituisce "grammazione in Python!", perché estrae i caratteri dalla posizione 3 alla fine della stringa
print(stringa[:]) # restituisce "Programmazione in Python!", perché estrae tutti i caratteri della stringa  
print(stringa[::2]) # restituisce "Pormzio nPto!", perché estrae i caratteri dalla posizione 0 alla fine della stringa, saltando di 2 in 2
print(stringa[-5:-2]) # restituisce "tho", perché estrae i caratteri dalla posizione -5 alla posizione -3 (-2-1)
print(stringa[::-1]) # restituisce "!nohtyP ni enimmargorP", perché estrae i caratteri dalla fine della stringa all'inizio, saltando di 1 in 1
print(stringa[:14:-1]) # restituisce "nohtyP ni enimmargorP", perché estrae i caratteri dalla posizione 13 alla posizione 0, saltando di 1 in 1

# strip(): rimuove gli spazi vuoti all'inizio e alla fine della stringa
stringa = "   caro amico   "
print(stringa.strip()) # restituisce "caro amico", perché rimuove gli spazi vuoti all'inizio e alla fine della stringa 

# replace(): sostituisce una parte della stringa con un'altra, ad esempio:
stringa = "ciao amico" 
print(stringa.replace("amico", "mondo")) # restituisce "ciao mondo", perché sostituisce "amico" con "mondo" nella stringa

# split(): divide la stinga in una lista secondo dei criteri, ad esempio:
stringa = "ciao amico, come stai ?"
print(stringa.split()) # restituisce ['ciao', 'amico', 'come', 'stai', '?'], perché divide la stringa in una lista di parole, usando lo spazio come separatore
print(stringa.split(",")) # restituisce ['ciao amico', ' come stai ?', perché divide la stringa in una lista di parole, usando la virgola come separatore

# Concatenzaione tra stringhe
a = "Mi"
b = "chiamo"
print(a + " " + b) # restituisce "Mi chiamo", perché concatena le stringhe a e b, aggiungendo uno spazio tra di loro    

# Stampare variabili in stringhe
eta = 20
print("Ho" + eta + "anni") # restituisce un errore, perché non è possibile concatenare una stringa con un intero
print(f"Ho {eta} anni") # restituisce "Ho 20 anni", perché utilizza la f-string per inserire il valore della variabile eta nella stringa