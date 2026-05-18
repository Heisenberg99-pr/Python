def elimina_caratteri(parola):
    diz_parola = {}
    firma = sorted(parola)
    lettere_ordinate = {}
    risultato = []
   
    i = 0
    for lettera in firma:
        lettere_ordinate[i] = lettera
        i+=1

    i = 0
    for lettera in parola:
        diz_parola[i] = lettera
        i+=1
    diz_parola = dict(sorted(diz_parola.items(), key=lambda elemeno: elemeno[1]))
    chiavi_parola = list(diz_parola.keys()) 
    chiavi_firma = list(lettere_ordinate.keys())

    for indice in chiavi_firma:
        if chiavi_parola[indice] <= indice:
            risultato.append(diz_parola[chiavi_parola[indice]])
    
    return "".join(risultato)

a = "ddabeceffgfh"
print(elimina_caratteri(a))

        
            

