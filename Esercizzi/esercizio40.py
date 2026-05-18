"""
Creare un programma che ragruppi le parole che sono anagrammi tra loro
"""
def ragruppa_anagrammi(parole):
    d = {}
    for parola in parole:
        sing = "".join(sorted(parola)) # genera al firma della parola
        a = d.get(sing,[]) # Genera una lista se sing non è in a 
        a.append(parola) #aggiunge la parola ad a 
        d[sing] = a # a viene aggiunta nella possizione sing nel dizionario
    return list(d.values())

def ragruppa_anagrammi_diz(parole):
    anagrammi = {}

    for parola in parole:
        chiave = "".join(sorted(parola))
        if chiave in anagrammi:
            anagrammi[chiave].append(parola)
        else:
            anagrammi[chiave] = [parola]
    return anagrammi 

lista = ["roma","taso","amor","sato","ramo","mora","osat","ciao"]
print(ragruppa_anagrammi(lista))
print(ragruppa_anagrammi_diz(lista)) 