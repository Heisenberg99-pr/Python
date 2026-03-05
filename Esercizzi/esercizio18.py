def pulisci_testo(testo): 
    '''
    Parametri: Testo

    La funzione avrà come parametro il testo e restituirà
    il testo senza punteggiatura e in minuscolo
    '''
    testo = testo.lower()

    for x in testo: 
        if x in [',','.','!','?',':']:
            testo = testo.replace(x,'')

    return testo; 

def conta_parole(testo): 
    parole = testo.split()
    frequenza = {}

    for x in parole: 
        if x in frequenza:
            frequenza[x] +=1
        else:
            frequenza[x] = 1
    return frequenza

def ordina_parole(frequenza): 
    parole = list(frequenza.keys()) # Recupero delle chiavi del dizionario
    n = len(parole)

    for i in range(n): 
        for j in range(i+1, n): 
            if(frequenza[parole[i]] < frequenza[parole[j]]) or (frequenza[parole[i]] == frequenza[parole[j]] and parole[i] > parole[j]):
                parole[i],parole[j] = parole[j], parole[i]
    parole_ordinate = []
    for parola in parole: 
        parole_ordinate.append((parola,frequenza[parola]))
    return parole_ordinate  

def ordina_parole_sorted(frequenza): 
    parole = list(frequenza.key())
    parole_ordinate = sorted(parole, key = lambda parola: (-frequenza[parola], parola))  
    risultato = []

    for parola in parole_ordinate: 
        risultato.append((parola, frequenza[parola]))
    
    return risultato


stringa = "La mela, la pera. La banana! Mela,mela."

print(f"Testo originale : {stringa}")
testo_pulito = pulisci_testo(stringa)

print(f"Testo pulito: {testo_pulito}")
frequenza = conta_parole(stringa)

print(f"Frequenza parole: {frequenza}")
testo_ordinato = ordina_parole(frequenza)

print(f"Parole ordinate: {testo_ordinato}" )
