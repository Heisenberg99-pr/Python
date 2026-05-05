'''
Creare una funzione che permetta il gioco dell'impiccato, semplificato quindi solo di parte funzionale 
'''

def impiccato(parola):
    terminata = False #permette di giocare fin tanto che non è stata vinta la partita o la partita sia stata persa 
    errori = 0 # contatore che tiene traccia degli errori dell'utente 
    lettere_parola = list(parola)
    soluzione = [lettere_parola[0]] + ["_"] * (len(lettere_parola) - 2) + [lettere_parola[-1]] # Calcolo della dimensione della soluzione

    while terminata == False and tentativi != 6:
        trovata = False
        print(f"Tentativi rimasti {6 - tentativi}\n") 
        print("Indovinare...\n" + " ".join(soluzione))
        tentativo = input("Inserisci una lettera...")

        if (len(tentativo)<= 1):
            for i in range(len(lettere_parola)):
                if tentativo == lettere_parola[i]:
                    soluzione[i] = tentativo
                    trovata = True
            if trovata == False:
                tentativi += 1
        else:
            if(tentativo == parola):
                terminata = True
                print("Hai vinto!!!")
            else:
                errori += 1

        if "_" not in soluzione:
           terminata = True
           print("Hai vinto!!!")
        elif errori == 6:
            terminata = True
            print("Hai Perso!!!")


parola = "Catamarano"
impiccato(parola)
print("Terminato")        
    
            
            


        
