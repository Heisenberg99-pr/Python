'''
creare una funzioni che rimuova i duplicati da una lista
'''

def rimuovi_duplicati(L):
    lista_senzaD = []

    for x in L:
        if x not in lista_senzaD:
            lista_senzaD.append(x)
    return lista_senzaD

L = [2,2,3,4,5,4,5,6]
print(f"La lista senza duplixati è: {rimuovi_duplicati(L)}")


    

