def fattoriale(n): 
    if n == 1:
        return n
    return n*fattoriale(n-1)
    
    

numero = 4
print(f"Il fattoriale di {numero} e' {fattoriale(numero)}")