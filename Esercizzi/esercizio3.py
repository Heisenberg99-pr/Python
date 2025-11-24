#Programma che somma le singole cifre di un numero 
somma = 0
n = input("Inserisci un numero... ")

for i in range(len(n)): 
    somma+=int(n[i])

print("La somma di ogni cifra e': ", somma)

#Metodo altrenativo di risoluzione

somma = 0
n = int(input("Digita un numero... "))

while n != 0:
    somma += n%10    # modulo
    n = int(n//10) # oppure n = n/10, divisione

print(somma)