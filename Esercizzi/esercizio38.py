"""
Creare un programma che permetta la generazione di numeri da 1 a 20 escludendo i numeri che sono
multipli di 3 e inserirli in una lista, contare i numeri pari e dispari presenti nella lista e mostrarli a video
trovare il minimo e massimo all'interno della lista generale.
"""

def crea_lista():
    """
    Parametri: Nessuno

    Crea una lista con elementi da 1 a 20 escludendo gli elementi che sono multipli di 3
    """
    lista = []

    for x in range(1,21):
        if(x%3 != 0): 
            lista.append(x)
    return lista

def conta_pd(lista):
    """
    Parametri: Una lista di numeri

    Conta il numero di numeri pari/dispari stampando a video il risultato
    """
    pari = []
    dispari = [] 
    count_pari = 0
    count_dispari = 0
    for x in lista:
        if x%2 == 0: 
            count_pari += 1
            pari.append(x)
        else: 
            count_dispari += 1 
            dispari.append(x) 
    print(f"Nella lista sono presenti {count_pari} numeri pari e sono: \n {pari}")
    print(f"Nella lista sono presenti {count_dispari} numeri dispari e sono: \n {dispari}")

def find_min_max(lista): 
    minimo = lista[0]
    massimo = lista[0]

    for elem in lista: 
        if elem > max:
            massimo = elem
        elif elem < min: 
            minimo = elem 
    print(f"Il massimo della lista e' {massimo} e il minimo e' {minimo}")

lista = crea_lista()
conta_pd(lista)
find_min_max(lista)


