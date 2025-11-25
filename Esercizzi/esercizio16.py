def unione(l1, l2):
    """
    Parametri: L0 e L1, due liste ordinate rispetto l'operatore <=

    Ritorna: la lista Lu contenente l'unione di L0 e L1. Gli elementi in
        Lu sono ordinati secondo <= e senza ripetizioni
    """
    #Si ricorda che l'algoritmo funziona se e solo se l1 e l2 sono ordinati secondo l'operatore <=
    lu = []

    i,j = 0,0

    while i < len(l1) and j < len(l2): 
        if (l1[i])<=(l2[j]):
            m = l1[i]
            i+=1
        else: 
            m = l2[j]
            j+=1
        
        if len(lu) == 0 or lu[-1] < m: 
            lu.append(m)
        
    while i < len(l1): 
        if len(lu) == 0 or lu[-1] < l1[i]: 
            lu.append(l1[i])
            i+=1
    
    while j < len(l2): 
        if len(lu) == 0 or lu[-1] < l2[j]: 
            lu.append(l2[j])
            j+=1
    return lu

l1 = [1,2,3,8,10]
l2 = [3,5,11,14,16,17]
print(unione(l1,l2))
