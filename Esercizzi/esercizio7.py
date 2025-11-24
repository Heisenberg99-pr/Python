# Usare una funzione argfind() che permetta di trovare la posizione di un 
# numero k all'interno di una lista L 
def argfind (L,k): 
    '''
        Parametri L: lista di numeri int o float, k: valore int o float 

        Stampa posizione della prima occorenza k in L
    '''
    for i in range( len(L)): 
        if k == L[i]:
            return i
    return -1
        
a = [5,2.4,8,9,0,3]
k = float(input("Inserisci un valore... ")) 
pos = argfind(a,k)
print(pos)