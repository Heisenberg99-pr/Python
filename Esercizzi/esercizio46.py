"""
Creare una funzione deep_mean, che calcoli la media dei numeri all'interno di una lista

es. lista = [1,2,3] ==> result = 1+2+3 / count = 3, in questo caso 

Allora scandire i singoli elementi della lista in un contatore [count] 

Ho una lista = [1,[2,3]] ==> 1 non è lista e allora somma = 1

"""

def deep_mean(lista, somma = 0,count = 0, restituisci_media = True):
    for elem in lista: # Scandisce ogni elemento della lista
        if type(elem)==list: # Se l'elemento della lista è una lista 
            sotto_somma, sotto_count = deep_mean(elem,restituisci_media = False) # Calcola la sotto somma della lista
            somma += sotto_somma # Somma la sotto_somma alla somma e il sotto count al count in modo da avere somma e count totali
            count += sotto_count
        else: # Altrimenti fa la normale somma
            somma+= elem;
            count+=1; 
    
    if not restituisci_media: # Se nella ricorsione fouri dalla ricorsione allora non restituisce somma e count altrimenti restituisce
        return somma,count
    
    if count == 0: # permette di ritornare allo stato di partenza 
        return 0
    return somma/count  # Alla fine restituisce la media
           
    
    
lista = [1,[2,3],[4,5]]
print(f"{deep_mean(lista)}")

# costo della funzione ==> temp = O(n) spaziale = O(n)

