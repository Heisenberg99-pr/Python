def bubble_sort(L): 
    """
    Il bubble sort, è un algoritmo di riordinamento che funziona tramite
    confronto di coppie di elementi adiacenti e scambiandoli se sono nell'ordine sbagliato
    """
    n = len(L) 

    for c in range (n-1): # campiona ogni elmento con l'aumentare di c
        ordinata = True # Flag che segna se la lista è ordinata 
        for i in range (n-1-c): #per n-1 volte non considerando c 
            if L[i] > L[i+1]: 
                    ordinata = False
                    L[i], L[i+1] = L[i+1], L[i]
        if ordinata: 
            break
    return L
 
lista = [1,2,3,4]

print(bubble_sort(lista))

#complessità temporale migliore O(n), peggiore O(n**2)
#Complessità spaziale O(1)