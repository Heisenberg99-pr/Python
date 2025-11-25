
"""
La funzione sort permette di ordinare una sequenza ritornando una nuova lista ordiata
il parametro key ha lo stesso significato che nella funzione merge
"""

a = ["zero", "uno", "due", "tre", "quattro", "cinque"]
b = sorted(a, key=lambda x: (len(x), x))
print(a)
print(b)