'''
Scrivere una funzione che rimuova i duplicati da un
lista L 
'''
def rimuovi_duplicati(L):
    '''
    Parametri: L una lista di elementi

    Restituisce la lista priva di qualsiasi duplicato
    '''
    lista_senza_duplicati = []
    for x in L:
        if x not in lista_senza_duplicati:
            lista_senza_duplicati.append(x)
    return lista_senza_duplicati

lista = [1,2,4,2,5,5,5]
print(f"La lista senza duplicati e': {rimuovi_duplicati(lista)}")