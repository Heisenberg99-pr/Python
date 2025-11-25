"""
Classificazione con k-Nearest Neighbor (kNN)

La classificazione è il processo di assegnare un elemento a una categoria
tra un insieme finito di categorie.

Il k-Nearest Neighbor (kNN) è un algoritmo che predice la classe di un nuovo campione
basandosi sulla classe più frequente tra i k campioni più vicini del dataset.
La vicinanza viene misurata tramite la distanza euclidea tra vettori delle caratteristiche.
"""

def eucdist(v, u):
    """
    Calcola la distanza euclidea tra due vettori v e u.
    
    Parametri:
        v, u: liste di float della stessa dimensione
    
    Ritorna:
        La distanza euclidea tra v e u
    """
    return (sum((x - y) ** 2 for x, y in zip(u, v)))**0.5


def argmax(L):
    """
    Trova la posizione dell'elemento massimo in una lista.
    
    Parametri:
        L: lista di numeri
    
    Ritorna:
        Indice dell'elemento massimo
    """
    return max(enumerate(L), key=lambda t: t[1])[0]


def moda(L):
    """
    Trova l'elemento più frequente in una lista di interi non negativi.
    
    Parametri:
        L: lista di interi positivi
    
    Ritorna:
        L'elemento più frequente in L
    """
    max_val = max(L)
    occorrenze = [0] * (max_val + 1)
    for x in L:
        occorrenze[x] += 1
    return argmax(occorrenze)


def kNN(F, labels, input_sample, k=5):
    """
    Classifica un nuovo campione usando l'algoritmo k-Nearest Neighbor.
    
    Parametri:
        F: lista di tuple (o liste) di feature float, ogni elemento rappresenta un campione
        labels: lista di etichette intere, labels[i] è l'etichetta del campione F[i]
        input_sample: tupla di feature del nuovo campione da classificare
        k: numero di vicini più prossimi da considerare (default 5)
    
    Ritorna:
        L'etichetta predetta per input_sample
        None se ci sono errori nei parametri
    """
    n, d = len(F), len(input_sample)

    # verifica che labels e F abbiano lo stesso numero di campioni
    if len(labels) != n:
        return None
    
    # verifica che ogni campione abbia la stessa dimensione di input_sample
    if any(len(f) != d for f in F):
        return None

    # calcola le distanze di input_sample da ogni campione, insieme alla loro etichetta
    distanze = [(eucdist(f, input_sample), lab) for f, lab in zip(F, labels)]

    # ordina le distanze e prendi i k più vicini
    k_nearest = sorted(distanze, key=lambda z: z[0])[:k]

    # estrai le etichette dei k vicini
    labels_in_nn = [lab for _, lab in k_nearest]

    # ritorna la moda delle etichette (classe più frequente)
    return moda(labels_in_nn)


# --------------------------
# Esempio di funzionamento
# --------------------------

# nomi dei campioni (solo per esempio, non usati nel kNN)
a = ["zero", "uno", "due"]

# etichette dei campioni
b = [0, 1, 2]

# feature dei campioni (ogni tupla rappresenta un campione)
c = [(9,3,4), (2,8,5), (1,1,1)]

# stampa dei campioni
for nome, label, features in zip(a, b, c):
    print(nome, label, features)

# campione da classificare
nuovo_campione = (3, 4, 3)

# applicazione del kNN
print (kNN(c, b, nuovo_campione, k=2))

