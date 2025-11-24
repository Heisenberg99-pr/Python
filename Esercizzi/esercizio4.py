#centrare una stringa 


a = input("Inserisci la prima stringa... ")
b = input("Inserisci la seconda stringa... ")

if len(a) > len(b):
    spazi_a, spazi_b = 0, (len(a)-len(b))//2
else:
    spazi_a, spazi_b = -(len(a)-len(b))//2, 0

print(" "*spazi_a+a)
print(" "*spazi_b+b)

