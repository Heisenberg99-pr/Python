"""
Scrivere un programma che:

1.  Pulisca il testo rimuovendo la punteggiatura e convertendo tutto in minuscolo.
2.  Conti la frequenza di ogni parola.
3.  Stampi le parole ordinate **prima** per frequenza (dalla più alta alla più bassa) e, a parità di frequenza, in ordine **alfabetico**.
"""


def pulisci_testo(testo): 
    """
    Parametri: testo variabile che contiene un testo

    Funzione: La funzione pulisce il testo rimuovendo pnutegiatura
    e convertendo tutti in minuscolo ritornando il testo pulito
    """
    testo = testo.lower() # Il testo viene portato tutto a minuscolo

    for char in testo:
        if char in ['.','!','?',';',':',',']:
            testo = testo.replace(char, " ")
    return testo

def conta_frequenza(testo):
    """
    Parametri: testo variabile che contiene un testo

    Funzione: La funzione conta la frequenza delle parole e ritorna frequenza
    """
    # la mela la pera la banana mela mela 
    #(chiave,frequenza) chiave = parola frquenza = contatore della frequenza
    # non bisogna considerare gli spazzi vuoti allora array di parole
    frequenza = {} # creazione di un dizionario
    parole = testo.split()

    for parola in parole:
        if parola in frequenza:
            frequenza[parola]+=1 # Se la parola è nel dizionario incrementa il contatore
        else: 
            frequenza[parola] = 1 # Se non presente nel dizionario la inserisce con valore iniziale
    return frequenza

def ordina_parole_per_frequenza(frequenza):
    parole = list(frequenza.keys())
    n = len(parole)

    for i in range(n): 
        for j in range(i+1 , n):
            if(frequenza[parole[i]]< frequenza[parole[j]] or frequenza[parole[i]] == frequenza[parole[j]] and parole[i] < parole[j]):
                parole[i],parole[j] = parole[j], parole[i]
    
    parole_ordinate = []

    for parola in parole: 
        parole_ordinate.append((parola,frequenza[parola]))
    return parole_ordinate

testo = "La mela, la pera. La banana! Mela, mela."
testo = pulisci_testo(testo)
print(testo)
print(conta_frequenza(testo))
print(ordina_parole_per_frequenza(conta_frequenza(testo)))


