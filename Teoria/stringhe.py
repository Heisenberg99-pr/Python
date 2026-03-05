'''
Introduzione alle stringhe in Python:

Un concetto fondamentale in Python, prima di iniziare, è quello che le stringhe
sono immutabili, ovvero non possono essere modificate
dopo essere state create. 
Se si vuole modificare una stringa, è necessario
crearne una nuova con le modiche desiderate.


Le stinghe in Python vengono contrassegnate da apici
[""] o [''], che valgono a dire la stessa cosa e la stampa
viene effettuata con la funzione print(). es:
'''
print("ciao mondo")
print('ciao mondo')

'''
Gli apici possono anche essere usati
nelle stringhe, ad esempio:
'''
print("Il cane di mattia e\' molto 'simpatico'")
print('Il cane di mattia e\' molto "simpatico"')    

'''
Ma devono essere diversi da quelli che racchiudono
la stringa.

le stinghe possono essere assegnate anche alle variabili
e stampate tramite la funzione print(), ad esempio:
'''
nome_variabile = "Davide"
print(nome_variabile)

'''
Le stringhe possono essere multilinea, ovvero possono
occupare più righe, e vengono raggiuse da tre apici
[""" """] o [''' '''], ad esempio:
'''
stringa_multilinea = """ciao adrea
come stai ?"""
print(stringa_multilinea)

'''
Inoltre c'è da dire che le stringhe in python, non sono altro
che array di caratteri e quindi possiamo accedere ad ogni singolo
carattere tramite un indice, ad esempio:
'''
stringa = "ciao amico"
print(stringa[3]) # stampa la lettera "o" che si trova alla posizione 3 della stringa

'''
Infatti, come negli array, possiamo scorrere i singoli caratteri della
striga tramite un ciclo for, ad esempio:
'''
stringa = "ciao amico"
for i in range (int(len(stringa))): # len(), restituisce la dimensione della stringa
    print(stringa[i]) #Permette di stampare solo un carattere nella posizione i

'''
Se vogliamo stampare la stinga al contrario, possiamo farlo
tramite gli indici negativi, ad esempio:
'''
stringa = "ciao amico"
for i in range (int(len(stringa))):
    print(stringa[-i-1]) #Permette di stampare solo un carattere nella posizione -i-1, che parte dall'ultimo carattere della stringa

#Perche meno 1 ? Perché se i parte da 0, -i-1 parte da -1, che è l'ultimo carattere della stringa
#e poi scorre verso l'inizio della stringa.