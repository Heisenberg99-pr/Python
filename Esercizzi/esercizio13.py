def intersezione(L1, L2):
    """
    Parametri: L1 e L2, due liste ordinate rispetto l'operatore <=

    Ritorna: la lista Lc contenente l'intersezione di L1 e L2. Gli elementi in
    Lc sono ordinati secondo <= e senza ripetizioni
    """
    Li = []

    i, j = 0, 0

    while i < len(L1) and j < len(L2):
        if L1[i] == L2[j]:
            if len(Li) == 0 or Li[-1] != L1[i]:
                Li.append(L1[i])
            i += 1
            j += 1
        elif L1[i] < L2[j]:
            i += 1
        else:
            j += 1

    return Li

a = [-10, -10,0, 1,2, 3, 3, 6, 8, 9, 9, 10,11]
b = [-10, -10, 0, 2, 3, 3, 4, 5, 6, 6, 10,11]

print(intersezione(a,b))