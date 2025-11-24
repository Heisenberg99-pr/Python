def argmax(L):
    """
    Parametri: L una lista di valori confrontabili tra di loro
    Ritorna: se |L| > 0, la posizione del massimo in L, altrimenti None
    """
    max_val, max_pos = None,None

    if len(L) != 0:
       for i, x in enumerate (L):
           if max_val == None or max_val < x:
            max_val, max_pos = x , i
       return max_pos
    
    return None

L = [6,3,4,9,0]

print(argmax(L))