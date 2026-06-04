"""
Creare una funzione deep_mean, che calcoli la media dei numeri all'interno di una lista

es. lista = [1,2,3] ==> result = 1+2+3 / count = 3, in questo caso 

Allora scandire i singoli elementi della lista in un contatore [count] 

Ho una lista = [1,[2,3]] ==> 1 non è lista e allora somma = 1

"""

def deep_mean(lista, somma = 0,count = 0, restituisci_media = True):
    for elem in lista:
        if type(elem)==list:
            sotto_somma, sotto_count = deep_mean(elem,restituisci_media = False)
            somma += sotto_somma
            count += sotto_count
        else:
            somma+= elem;
            count+=1; 
    
    if not restituisci_media:
        return somma,count
    
    if count == 0:
        return 0
    return somma/count
   
           
    
    
lista = [1,[2,3],[4,5]]
print(f"{deep_mean(lista)}")

# costo della funzione ==> temp = O(n) spaziale = O(n)

