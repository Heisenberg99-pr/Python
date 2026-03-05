'''
Complessità Temporale e Spaziale

La complessità temporale di un algoritmo è una misura di quanto tempo impiega a completare 
la sua esecuzione in funzione della dimensione dell'input.
Non si misura il tempo reale in secondi, ma come cresce il numero di operazioni quando 
aumenta la dimensione dei dati in ingresso.

Per descrivere questa crescita si utilizza la notazione asintotica, in particolare 
la notazione Big O, che indica il comportamento dell'algoritmo per input molto grandi.

Esempi comuni di complessità temporale sono:

O(1) → tempo costante, l'algoritmo impiega sempre lo stesso tempo indipendentemente dall'input.

O(n) → tempo lineare, il tempo cresce proporzionalmente alla dimensione dell'input.

O(n²) → tempo quadratico, tipico degli algoritmi con cicli annidati.

O(log n) → tempo logaritmico, tipico di algoritmi che dimezzano il problema ad ogni passo (come la ricerca binaria).

La complessità spaziale di un algoritmo è invece una misura di quanta memoria utilizza durante l'esecuzione 
in funzione della dimensione dell'input. 
Questa include sia la memoria necessaria per memorizzare i dati di ingresso sia quella utilizzata per variabili, strutture dati 
o chiamate ricorsive.

Anche la complessità spaziale viene espressa con la notazione Big O, ad esempio:

O(1) → memoria costante.

O(n) → la memoria cresce proporzionalmente alla dimensione dell'input.

Lo studio della complessità temporale e spaziale permette di confrontare algoritmi diversi e scegliere quello più efficiente, soprattutto 
quando si lavora con grandi quantità di dati.

Come possiamo calcolare la complessità temporale e spaziale di un algoritmo?

Per calcolare la complessità temporale di un algoritmo, si analizzano le operazioni 
eseguite in relazione alla dimensione dell'input.
Si contano le operazioni fondamentali (come assegnazioni, confronti, cicli) e si esprime 
la crescita del numero di operazioni in funzione della dimensione dell'input, utilizza la notazione Big O
prima introdotta, andiamo a fornire quindi qualche esempio:
'''

def ricerca(D,k):
    """
    Paramentri: D una lista che implementa un dizionario come lista di coppie (chiave,valore)
                k una potenziale chiave
    Rirtona la posizione in D della coppia che ha per chiave k, altrimenti None
    """
    for i in range (len(D)): 
        if (D[i][0] == k): 
            return i
        else: 
            return None
        #complessità temporale O(len(D)), quindi dipende dalla lunghezza di D
        #complessità spaziale O(1) perché utilizza solo una quantità costante di memoria aggiuntiva

'''
Osservazione: Le funzioni ricorsive hanno sempre una complessità spaziale almeno O(n)
a causa del numero di frame sullo stack delle chiamate
'''
# cosa sono i frame sullo stack delle chiamate?
# Quando una funzione viene chiamata, viene creato un frame sullo stack delle chiamate
# il frame contiene le variabili locali e lo stato della funzione
# Quando la funzione termina, il frame viene rimosso dallo stack

# Esempio di una funzione ricorsiva

def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n * fattoriale(n-1)

#complessità temporale O(n) perché la funzione viene chiamata n volte
#complessità spaziale O(n) perché ci sono n frame sullo stack delle chiamate, uno per ogni chiamata ricorsiva