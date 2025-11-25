def ricerca_binaria_lx(L, k):
    n = len(L) 

    lx, rx = 0, n

    while lx <= rx-1: # fin tanto che lx non è uguale a rx, quindi n-1 
            cx = int( (lx + rx)/2 ) # cerca la posizione possibile di k

            if L[cx] == k and (cx == 0 or L[cx-1] < k ): #Per cercare il k più a sinistra
                  return cx # In generale la funzione controlla se il numero trovato è uguale a k, nel caso lo restituisce
            
            elif k < L[cx]: 
                  rx = cx # Restringe il campo escudendo tutti i numeri dopo cx
                    # esempio 1,2,3,10,11,17 cx = 3 k = 2 [2 < 10] rx = n => rx = 3
                    # quindi il nuovo controllo verrà effetuato su elementi 1,2,3,10
            else: 
                  lx = cx+1 # Restinge il campo eliminando tutti i numeri prima di cx
                    # esempio -10,1,2,3,10,11 cx = 2 k = 10 [10 > 2] lx = cx+1 => lx = 3, esclude la posizioe 2 già inclusa prima 
                    # quindi il nuovo controllo verrà effetuato su elementi 3,10,11


    return -1 

L = [0,1,4,5,1,6,8]
print(L,1)