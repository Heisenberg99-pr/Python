def is_palindroma(stringa):
    i,n = 0, len(stringa)
    isPalindroma = True

    while i < n//2 and isPalindroma == True:
        if stringa[i] != stringa[-i-1] : # Confronta con una coppia di carratteri simmetrici
            return False
        else: 
            i+=1
    return True

stringa = input("Inserisci una frase... ")
print(f"{is_palindroma(stringa)}")