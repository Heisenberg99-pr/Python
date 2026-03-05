def lunghezza_parole(testo):
    parole = testo.split() #Divide il testo in un array di parole[], criterio (" ")
    len_parole = {} # Crea un dizionario len_paorle = {} vuoto 
    for parola in parole: 
        len_parole[parola] = len(parola) # Se la parola non è nel dizionario viene inserita associata alla lunghezza
    return len_parole # Ritrona il dizionario
# Costo Temporale O(n)

testo = "ciao mondo"
len_parole = lunghezza_parole(testo)
print("La lunghezza delle parole e': ")
print(f"{len_parole}")
