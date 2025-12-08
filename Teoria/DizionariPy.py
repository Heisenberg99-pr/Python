"""
Un Dizionario è una struttura dati estratta composta da coppie (x,y) con la
proprietà che le chiavi k, non siano ripetute, permettendo di creare associazioni
tra le chiavi [k] e i valori [v].

Operazioni: 

Creazione: cerare un dizionario vuoto
Lettura/Ricerca: data una chiave, ritorna il valore ad essa associata
Aggironamento: data una coppia (k,v1), se k è una chiave del dizionario,l'operazione sostituisce
il vecchio valore con v1
Inserimento: inserisce una nuova coppia (k,v) nel caso k non esiste già
Cancellazione: Data una chiave k, cancella dal dizionario la coppia con k
"""

def creazione():
    """
    Ritorina un dizionario vuoto
    """
    return []
    #complessita spaziale e temporale O(1)

def ricerca(D,k):
    """
    Parametri: D una lista che implementa un dizionario come lista di coppie
    (chiave,valore) k una potenziale chiave
    
    Rirtona la posizione in D della coppia che ha per chiave k, altrimenti None
    """
    for i in range (len(D)): 
        if (D[i][0] == k): 
            return i
        else: 
            return None
        #complessità temporale O(len(D))
        #complessità spaziale O(1)

def inserimento(D,k,v):
    """
    Paramentri: D una lista che implementa un dizionario come lista di coppie (chiave, valore)

    k una chiave
    v un valore

    Ritorna None

    Effetti collaterali: se k è una chiave, sostituisce il valore con v altirmenti aggiunge la coppia (k,v)
    """
    p = ricerca(D,k)
    if p == None:
        D.append((k,v))
    else: 
        D[p] = (k,v)
    
    return None
    # complessità temporale O(len(D))
    # complessità spaziale O(1)

def appartiene(D,k): 
    """
    Paramentri: D come lista che implementa un dizionario come lista di coppie (chiave,valore)
                k una potenziale chiave
    Ritorna True se e sole se k è una chiave di D
    """
    if ricerca(D,k) == None:
        return False
    else:
        return True
    # complessità temporale O(len(D))
    # complessità spaziale O(1)

def cancellazione(D,k): 
    """
    Paramentri: D una lista che implementa un dizionario come lista di coppie (chiave, valore)

    k una chiave

    Ritorna None

    Effetti collaterali: se k è una chiave, cancella da D la coppia conq quella chiave k
    """
    p = ricerca(D,k)

    if p != None: 
        del(D[p])
    
    # complessità temporale O(len(D))
    # complessità spaziale O(1)
d = creazione()
inserimento(d, "uno", 1)
inserimento(d, "zero", 0)
inserimento(d, "uno", 1.0)
inserimento(d, "due", 2.0)
inserimento(d, 3, "tre")
cancellazione(d, "due")
print(appartiene(d, "zero"))

print(d)