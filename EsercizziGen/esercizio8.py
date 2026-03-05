def somma_elementi_unici(A,B):
    somma = 0
    count = 0
    indice = 0
    list = []
    for elemento in A:
        list.append(elemento)
    for elemento in B:
        for elemento2 in list:
            if(elemento == elemento2):
                count = 1
                break
        if count == 0:
            list.append(elemento)
        else:
            list.remove(elemento)
            count = 0
    for elemento in list:
        somma += elemento
    return somma

A = [1, 2, 3]
B = [3, 4, 5]
print(f"La somma degli elementi unici e': {somma_elementi_unici(A,B)}")

