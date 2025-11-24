def intersezione(l0,l1):  
    """
        Parametri: L0 e L1, due liste
        Ritorna una nuova lista contenente tutti i valori presenti sia in L0 che in L1;
        la lista ritornata non contiene duplicati
    """

    I = []

    for x in l0:
        if x in l1 and x not in I:
           I.append(x)
    
    return I

l0 = [4,3,2,5]
l1 = [3,6,3,4]

print(intersezione(l0,l1))
