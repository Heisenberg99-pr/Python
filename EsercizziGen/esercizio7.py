def conta_elementi_intersezione(A,B):
    intersezione = {}
    count = 0
    for elemento in A: 
        intersezione[elemento] = True

    for elemento in B:
        if intersezione.get(elemento,False):
            count+=1
            intersezione[elemento] = False # Cosi non riconta l'elemento nel caso viene trovato una seconda volta
    return count

A = [1, 2, 3, 4]
B = [3, 4, 5, 4]
print(conta_elementi_intersezione(A,B))