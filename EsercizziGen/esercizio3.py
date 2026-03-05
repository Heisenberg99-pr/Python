def ordina_parole(stringa): 
    parole = stringa.split()
    n = len(parole)
    # Applicazione del bubble sort.
    for i in range(n-1): 
        for j in range(n-1-i): 
            if parole[i] < parole[j]: 
                parole[i], parole[j] = parole[j], parole[i]
    return parole

stringa = "ciao mondo andorra come va tutto bene"

print(f"{ordina_parole(stringa)}")