def argmax( L,i ):
        """
        Parametri: L una lista di valori confrontabili tra di loro, un indice della lista (i<n)
        Ritorna la posizione del massimo tra gli elementi L[i], L[i+1],...,L[n-1] se n > 0, altrimenti None
        
        Lo si vuole fare in modo ricorsivo: 

        Prima di tutto bisogna sapere, cosa è la ricorsione ? 

        La ricorsione è un tecnica di programmazione e di definizione composta da 
        due parti, un caso base, che specifica dierttamente il risulatato per
        un caso speciale e un caso ricorsivo, che definisce la risposta in 
        termini della risposta alla domenada per qualche altro input con una
        versione più semplice dello stesso problema.

        Ora risolviamo il problema soprastante: 
        """
        
        n = len(L) # Memorizza la lunghezza della stringa

        if n == 0:
            return None # Caso in cui la lista sia vuota
        if i == n-1:
            return i # Caso in cui la lista abbia almeno un elemento

        #Caso base

        p = argmax(L,i+1)

        if L[i] > L[p]: # Qui confronta gli elementi nelle posizioni i e p ritornando la posizine maggiore
            return i
        else: 
            return p 
        
       

a = [ 0, 0,11, 1, 2, 8, 10]
print( argmax(a, 0) )     

"""
Calcolare la complessità temporale della funzione argmax ricorsiva: 

Sia T(n) il numero di operazioni eseguite dalla dunzione su una
sottolista di dimensione n. Allora per le opportune costanti c0 e c1

T(n) = c0 se n<2 caso in cui la funzione termini subito
T(n) = c1 + T(n-1) negli altri casi

Sviluppando T(n) = (n-1)c0 + c1 che è O(n)

La complessità sapziale invece è data dal numero massimo di frame sullo
stack delle chiamate, ovvero n ( dato che dipende dalla linghezza di L).

quindi la complessita spaziale e temporale sono entrabe O(n)
ciò significa che al variare di n (quindi in funzione di n) aumentano sia
la complessità spaziale che la temporale in egual modo
"""
        
