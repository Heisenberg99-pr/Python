'''
Scrivere un programma che chieda due input [nome] e [età] 
restituiendo l'età tra [etaPost] anni.
'''
def etaTra(eta, anni):
    etaFin = eta + anni
    return etaFin


nome = input("Inserisci il tuo nome... ")
eta = int(input("Inserisci la tua età... "))
anni = int(input("Inserisci di quanti anni vuoi aumentare la tua età per vedere l'età tra tot anni..."))
print(f"Ciao {nome}, la tua età fra {anni} è {etaTra(eta,anni)} anni")

# Temp O(1) Spaz O(1)