"""
Date due liste A e B, restituire la somma degli elementi che fanno parte dell'intersezione delle due liste

Esempio

Input: `A = [1,2,3,4,5], B=[4,5,7,8,9]`
Output: `C = 9 (4+5)`
"""

def somma_intersezione(A,B):
    """
    Parametri: A e B due liste di numeri interi

    Esecuzione: Restituisce l'intresezione tra A e B e somma gli 
    elementi dell'intersezione restituendo il risultato
    """
    intersezione = []
    for elem in A:
        if elem in B:
            if elem not in intersezione:
                intersezione.append(elem)
    somma = 0
    for elem in intersezione:
        somma+=elem
    return somma

def somma_intersezione_dizionario(A,B):
    elementi = {}

    for elemento in A:
        elementi[elemento] = True #Indica "l'elemento esiste" e l'elemento è usato come chiave 
    
    somma = 0
    for elemento in B:
        if elementi.get(elemento, False): #se elemento non è presente restituisce False altrimenti elemento
            somma += elemento
    return somma
            

A = [1,2,3,4,5]
B = [4,5,8,1,9]
print(somma_intersezione(A,B)) 



