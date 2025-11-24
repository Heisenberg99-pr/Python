# in questo esercizio, vogliamo usaare le variabili in modo diverso
# cercando di capire il loro utilizzo
# algoritmo che calcola il logaritmo di un numero in base 2

n = 13; 
k = 0
while n > 2:
    n = n/2; 
    k+=1; 
print("Il logaritmo in base 2 di 13 e': ", k)

# ora vogliamo dare in assegnazione un valore in input usando [input()]

num = input("Inserisci il numero un numero: ")
num = int(num) # visto il problema sotto scritto, convertiamo la stringa in un intero [int(variabile)], ciò si puo fare anche per altre tipologie di variabili
k = 0; 
while num >2: # in questa riga c'e' un errore in quanto num è una stinga e come tale non puo essere confrontata con un intero
    num /=2 
    k+=1

print("il logaritmo in base 2 di ", num, " e': ", k)