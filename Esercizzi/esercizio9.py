def second_max( L ): 
      '''
        Parametri: L una lista di numeri
        
        Ritorna il secondo valore più grande della lista L;
        se la lista contiene almeno due elementi, None altrimenti.
        
        Nel caso di due massimi, la funzione ritorna il massimo

        Esempi:
        
        se L = [3, 1, 4, 2, 0], la funzione ritorna 3
        se L = [3, 1, 4, 2, 4], la funzione ritorna 4
    '''
      cor_max = 0
      sec_max = 0
      if len(L)<2: 
            return None
      else:
            for i, x in enumerate( L ): #enumerate, permette di ottenere sia l'indice che l'elemento
                    if cor_max <= x:
                           sec_max = cor_max 
                           cor_max = x
            return sec_max
      
a = [3,4,0,1,2,7]
b = [3,7,0,6,7,5]

print(second_max(a))
print(second_max(b))

