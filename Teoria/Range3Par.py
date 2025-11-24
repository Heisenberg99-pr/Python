'''
    La funzione range si può implementare anche con tre parametri 
    range(start,stop,step)

    start: punto di inizio
    step: ad ogni iterazione aggiunge [val]
    stop: punto in cui si deve fermare

    in seguito un esempio:
'''
L = [2,4,5,6,7,4,5,3,4]
lista = []
for x in range(0,len(L),2):
    lista.append(L[x])

print(lista)
    
