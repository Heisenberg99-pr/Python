def clonazione_profonda(L): 
    """
    La clonazione profonda ci permette di poter clonare liste che sono
    presenti in altre liste, che altrimenti verrebero trasformate in alias
    (vedere capitolo sulle liste). Ciò si fa tramite l'uso della ricorsione:
    """
    if type(L) != list:
        return L
    
    Lc = []

    for e in L:
        Lc.append(clonazione_profonda(e))
    
    return Lc
 

Lista = [[0,[1,2,[3,4]]], [5,[6,[7,8]]]]
Lista_clonata = clonazione_profonda(Lista)

Lista_clonata[0][0] = "uno"
print(Lista)
print(Lista_clonata)