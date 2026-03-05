def partial_bouble_sort(L, k):
    '''
    Paramentri: una lista con elementi confrontabili; un intero k
    Ritorna: La lista dei k elementi più piccoli di L 
    '''
    # Ragionamento: abbiamo una Lista L nella quale dobbiamo trovare i k elementi più piccoli nella lista
    # k quindi saranno gli elementi che dobbiamo trovare 
    n = len(L) # Creazione di un array n, che tiene tarccia della lunghezza di L
    lst = [] # Creazione di un array vuoto che conterrà il risultato
    # Applichiamo quindi il bubble sort, per i primi k elementi, complessità temporale O(n^2)
    for x in range (k): 
        for i in range(n-1-x):
            if L[i] > L[i+1]: 
                L[i], L[i+1] = L[i+1], L[i]
        
    for i in range (k): 
        lst.append(L[i]) # Inseriamo il risultato del bubble sort nell'array lst, che conterrà i primi k elementi minori
               
    return lst # Ritorna il risultato della funzione

L = [1,2,5,4,3]
k = 3
print(partial_bouble_sort(L,k)) 