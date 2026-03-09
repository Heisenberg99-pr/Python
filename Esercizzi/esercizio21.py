
'''
Scrivere un programma che chiede all’utente di inserire un numero 
intero positivo e stampa a video la somma di tutti i numeri interi 
da 1 a quel numero.
'''

numero = int(input("Inserisci un numero intero:"))
somma = 0
for i in range(numero+1):
    somma+=i
print(f"La somma dei numeri da 1 a {numero} e' {somma}")
