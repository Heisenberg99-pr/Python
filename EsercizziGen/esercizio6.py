def somma_intersezione_whit_dict(A,B): 
    elemento_dict = {}
    for elemento in A: 
        elemento_dict[elemento] = True

    somma = 0 
    for elemento in B:
        if elemento_dict.get(elemento, False): # Dice se elemento.get (prende chiave) è presente nel dizionario restituisci True altirmenti False, se True somma
            somma+=elemento
            elemento_dict[elemento] = False
    return somma

A = [1, 2, 3, 4]
B = [3, 4, 5]
print(somma_intersezione_whit_dict(A,B))