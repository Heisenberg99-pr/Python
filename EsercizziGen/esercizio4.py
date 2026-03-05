def inverti_parole(stringa):
    inversa = stringa[::-1] # Permette di invertire una stringa costo di O(n)
    return inversa

stringa = "ciao mondo"
print(f"{inverti_parole(stringa)}")    