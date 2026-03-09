'''
Variabili in Python
Una variabile, in generale, è un contenitore che permette
di memoriazzare un valore, che può essere di diversitipi:

- numeri interi (int): rappresentano numeri senza la parte decimale, ad esempio: 1, 2, 3, -1, -2, -3
- numeri decimali (float): rappresentano numeri con la parte decimale, ad esempio: 1.5, 2.3, -1.2
- stringhe (str): rappresentano sequenze di carratteri, ad esempio: "ciao", "Python", "123" (approfondimento su stringhe.py)
- booleani (bool): rappresentano i valori di verità, ad esempio: True, False
- liste (list): rappresentano collezioni di valori, ad esempio: [1, 2, 3], ["ciao", "Python"], [1, "ciao", True]
- tuple (tuple): rappresentano collezioni di valori immutabili, ad esempio: (1, 2, 3), ("ciao", "Python"), (1, "ciao", True)
- dizionari (dict): rappresentano collezioni di coppie chiave-valore, per esempio: {"nome": "Mario", "età": 30}, approfondimento su dizionari.py
- None: rappresenta l'assenza di un valore, ad esempio: None

Per la creazione di una variabile, si segue la forumula:

nome_variabile = [valore]

Bisogna dire che in Python non è necessario dichiarare il tipo di variabile
garzie al fatto che Python è un linguaggio dinamicamente tipizzato, ovvero
il tipo di variabile viene determinato automaticamente in base al valore assegnato alla variabile

Esempi di creazione di variabili:
'''

numero = 10
stringa = "Il cane di andrea è socevole"
booleano = True
booleano2 = False
numero_decimale = 3.14
lista = [1,2,"catanzaro", True, 3.14]
tupla = (1,2,"catanzaro", True, 3.14)
dizionario = {"nome": "mario", "età": 30} #rapporto chiave->valore
variabile_vuota = None

'''
Regole:

- Il nome della variabile deve iniziare con una lettera o underscore
- Il nome della variabile non deve contenere spazzi
- Il nome della variabile non deve essere abiguo, ma significativo, ad esempio: numero, nome, età, etc
- Il nome della variabile deve essere unico, non può quindi esistere numero e numero
- Il nome della variabile non deve essere una parola riservata, ad esempio: if, else, while, for, def, class, import, etc

Le variabili possono essere castate ( detto casting ), ciò costringe le variabili a essere di quel tipo, ad esempio:
'''
stringa = "19"
numero = 10
print(int(stringa)+numero) # restituisce 29, perché converte la stringa "19" in un intero e poi somma con il numero 10

'''
 Ora vogliamo che queste variabili possano contenere
 qualcosa che l'utente inserisce da tastiera, questo
 lo possiamo fare tramite la funzione input(), il quale va a 
 leggere l'input dell'utente e lo restituisce come stringa
'''

nome = input("Inserisci il tuo nome:")
print("Il tuo nome e': " + nome)

'''
Se volessimo invece inserire un qualsiasi altro tioi di dato, dovremmo fare
un'operazione di casting all'input, ad esempio:
'''

numero = int(input("Inserisci un numero intero: "))
print(f"Il numero inserito e': {numero} e il suo tipo e': {type(numero)}")
