def merge(l1,l2):
    """
    Parametri: l0 e l1 liste ordinate
    Output: M, Lista ordinata contenente tutti elementi di l0 e l1
    """
    # In questo esericizio sfrutteremo lo stesso algoritmo usato per l'unione
    # ( Vedi esercizio 16 )
    M = []

    i,j = 0,0

    while i < len(l1) and j < len(l2): 
        if l1[i]  < l2[j]: 
            m = l1[i]
            i+=1
        else: 
            m = l2[j]
            j+=1
       # Qui non serve controllare se esiste un elemento già presente a differenza dell'esercizio 16
        # Nel quale era invece specificato dalla docstring l'assenza di doppioni
        M.append(m)

        while i < len(l1): 
            M.append(l1[i])
            i+=1
        while j < len(l2): 
            M.append(l2[j])
            j+=1
        
    return M

a = [0,1,1,4,5,6,6,7,7]
b = [1,2,2,3,6,7,8,9,9]
print(merge(a, b))
