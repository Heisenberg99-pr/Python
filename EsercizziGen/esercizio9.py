def rimuovi_caratteri(a):
    '''
    Docstring for rimuovi_caratteri
    
    Parametri: stinga a

    rimuove tutti i caratteri che non sono in ordine lessicografico in a 
    ritornando infine la stinga pulita
    '''
    risultato = [a[0]]
    for i in range(1,len(a)):
        if  a[i] >= risultato[-1]: # Verifica se il carattere in a mantiene l'ordine se si append, altrimenti viene scartato 
            risultato.append(a[i])

    
    return "".join(risultato)

a = "ddabeceffgfh"
print(rimuovi_caratteri(a))
        