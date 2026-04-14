"""
La complessità spaziale di un algoritmo è una misura della 
quantità di memoria extra necessaria per eseguire l'algoritmo,
oltre alla memoria necessaria per memorizzare l'input.
"""
def second_max( L ):
    """
    Parametri: L una lista di numeri

    Ritorna il secondo valore più grande della lista L;
    se la lista contiene almeno due elementi, None altrimenti.

    Nel caso di due massimi, la funzione ritorna il massimo
    """

    n = len(L)
    if n >= 2:
            max1 = max(L[0], L[1])      # O(1) tempo; O(1) spazio extra
            max2 = min(L[0], L[1])      # O(1) tempo; O(1) spazio extra
            for x in L[2:]:             # per n-2 volte; O(n) spazio extra per slicing
                    if x > max1:        # O(1) tempo; O(1) spazio extra
                            max2 = max1
                            max1 = x
                    elif  x > max2:
                            max2 = x
            return max2
    else:
            return None
        
        # Complessità temporale: O(n)
        # Complessità spaziale: O(n), togliendo slicing O(1)
        # Indicizando invece la lista avremmo una complessità di O(1)

L = [3, 1, 4, 1, 5, 9]
print(second_max(L))