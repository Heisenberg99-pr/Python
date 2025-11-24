a = [2, 3, 5, 7]
somme = []

for i in range(len(a)):
    
    if((i+1) < len(a)):
        somme.append(a[i]+a[i+1])
    else:
        somme.append(a[i]+a[-len(a)])
    

print(somme)