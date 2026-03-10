'''
Si richiede di scrivere un programma che data una qualsiasi stringa
stampa a video le vocali contenute 
'''

def vocali(stringa): 
    countVocali = 0
    vocali = "aeiouAEIOU"
    for i in stringa: 
        if i in vocali: 
            countVocali += 1
    return countVocali

stringa = input ("Inserisci una stringa...")
print(f"La stringa contiene {vocali(stringa)} vocali")
