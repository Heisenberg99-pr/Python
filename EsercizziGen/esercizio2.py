def ordina_parole(parole):
    # Ordiniamo con sorted parole specifichiamo sorted(cosa ordinare, secondo cosa ordinare es. lambda x(elemento): (chiave di confronto))
    # es chiave di confronto lambda parola: (len(parola), parola) ordina quindi per valore crescente la lunghezza della parola se uguale confrota le parole
    # Se volessimo ordinarle in modo decrescente aggiungere il parametro reverse = True
    parole_ordinate = sorted(parole, key = lambda parola: (len(parola),parola))

    risultato = []
    for x in parole_ordinate: 
        risultato.append(x)
    return risultato


parole = ["casa", "a", "sole", "albero", "bo"]
parole_ordinate = ordina_parole(parole)
print(f"{parole_ordinate}")