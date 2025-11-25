
def merge_sort(L,key = lambda x:x, lx = 0, rx = None): # Rende facoltativi i parametri lx e rx, se omessi ordinerà la lista intera
    # Permette di personalizzare il criterio di ordinamento introducendo una funzione opzionale key che definisce il valore dell'elemento della lista
    # da usare nel confronto all'interbi della funzione marge, Di default questa funzione è l'identità
    # quindi python non riordinerà in base agli elementi stessi, ma in base ai valori restituiti dalla funazione lambda => f = lambda x: x**2 usando il valore di uscita come criterio
    """
    Parametro: L, una lista di elementi con <=
    lx < rx. due indici in L
    Ritorna None

    Effetto collaterale: ordina gli elementi di L dalla posizione lx a rx-1
    """
    def merge(L, lx, cx, rx):
        """
        Parametri: L una lista di elementi confrontabili con <=
            lx <= cx < rx, tre indici di L e tali che
            L[lx] <= L[lx+1] <= ... <= L[cx-1] e
            L[cx] <= L[cx+1] <= ... <= L[rx-1]
        Output: None

        Effetto collaterale: al termine della funzione
        L[lx] <= L[lx+1] <= ... <= L[rx-1]
        """
        M = []

        i, j = lx, cx # Considera la prima parte dell'array

        while i < cx and j < rx:
            if L[i] <= L[j]:
                M.append(L[i])
                i += 1
            else:
                M.append(L[j])
                j += 1

        #Inserisce gli elementi rimanenti
        while i < cx:
            M.append(L[i])
            i += 1
        while j < rx:
            M.append(L[j])
            j += 1

        for k in range(len(M)):
            L[lx + k] = M[k]
    
    if rx == None:
        rx = len(L)

    if lx >= rx - 1:  # se lx è maggiore di rx - 1, la funzione ritorna direttamente None
        return None

    cx = (lx + rx) // 2  # divisione intera

    # effettua il riordinamento delle prime due metà per poi unirle tramite la funzione merge
    merge_sort(L,key, lx, cx)
    merge_sort(L,key, cx, rx)
    merge(L, lx, cx, rx)

a = [6,2,3,1,9,0,1,2,6,5,3,8,1]
merge_sort(a, key = lambda x:x[1])
print(a)