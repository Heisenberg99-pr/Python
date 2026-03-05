def raggruppa_anagrammi(parole): 
        anagrammi = {}

        for parola in parole: 
            chiave = ''.join(sorted(parola))
            
            if chiave in anagrammi: 
                anagrammi[chiave].append(parola)
            else:
                anagrammi[chiave] = [parola]
            
        return anagrammi 

parole = ["roma", "taso", "amor", "sato", "ramo", "mora", "osat", "ciao"]
anagrammi_raggruppati = raggruppa_anagrammi(parole)
print("Anagrammi raggruppati :")
print(anagrammi_raggruppati)