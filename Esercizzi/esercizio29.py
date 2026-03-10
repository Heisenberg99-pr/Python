print("Inserisci 5 numeri...")
lista = []
for i in range(5):
    numero = int(input(f"Inserisci il {i+1} numero..."))
    lista.append(numero)

lista.sort()
print(lista)