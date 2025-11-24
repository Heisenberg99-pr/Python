n, i = 10, 0 #assegnazione multipla

print(n,i)

#tupla (t)
t = 10,5 #impacchettamento, packing

print(type(t)) #Stampa il tipo di var di t

print(t) #stampa il contenuto della tupla t 

#Per le tuple sono definite tutte le operazioni sulle stringe, come le stringhe sono immutabili

n, i = t #spacchetamento, unpacking, di t in 2 variabili n e i  
print(n, i) #stampa n ed i

t = (0,3.14,('python', 0,'stringa'), 9) #le tuple possono contenere più valori anche di differente tipo come anche altre tuple

print(t[0],t[2]) #indicizzazione 