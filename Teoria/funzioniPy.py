def cumsum( L ):  #Definire una funzione def nome_funzione( parametro )
                  #Si possono definire anche più paramentri allinterno di una funzione

    '''
        Parametri: L una lista di numeri (int e float)

        Stampa la lista delle somme comulative
    '''
    #DocString: è una stringa che spiegherrà il funzionamento della funzione
    # é di buona norma infatti spiegare il funzionamento delle funzioni
    # per chi le dovrà poi usufroire in futuro

    somme = [] #cerazione di una lista vuota di nome somme 
    
    for x in L: #x, variabile locale
        if somme == []:
            somme.append(x)
        else: 
            c = somme[-1] + x # c, variabile locale 
            somme.append(c)
    
    return somme #restituisce il risultato contentuto in somme, interrompe la funzione

#esempio di applicazione 

a = [6,3,4,1,3]
b = cumsum(a) # Chiamata alla funzione cumsum con passaggio di parametro a
print(b)

help(cumsum) #restituisce la docstring della funzione 
