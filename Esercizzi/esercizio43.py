def intersezione(A,B):
    
    if len(A) == 0 or len(B) == 0:
        return 0 
    
    elementi_int = []
    diz_a = {}
    for elemento in A:
        diz_a[elemento] = True
    
    for elemento in B:
        if diz_a.get(elemento, False):
            elementi_int.append(elemento)
    
    elementi_int = set(elementi_int)
    return len(elementi_int)
    

def unione(A,B):
    
    if len(A) == 0 or len(B) == 0:
        return 0
    
    elementi_uni = []

    for elemento in A:
        elementi_uni.append(elemento)
    for elemento in B:
        elementi_uni.append(elemento)
    
    elementi_uni = set(elementi_uni)

    return len(elementi_uni)

A = [2,5,6,8,7,4]
B = [4,5,2,1,4,7,8]

print(f"Il coefficente di Jaccard e': {intersezione(A,B)/unione(A,B)}")


