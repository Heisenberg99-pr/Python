def insieme_potenza(elementi, indice = 0, sottoinsieme_corrente = []):
    
    if indice == len(elementi): 
        print(sottoinsieme_corrente)
        return 
    
    insieme_potenza(elementi, indice + 1,sottoinsieme_corrente )
    sottoinsieme_corrente.append(elementi[indice])
    insieme_potenza(elementi, indice+1, sottoinsieme_corrente)
    sottoinsieme_corrente.pop()

insieme_potenza(['A','B','C'])