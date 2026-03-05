
def bubble_sort(a):
    stinga_ordinata = list(a)
    for i in range(len(stinga_ordinata)-1):
        for j in range(len(stinga_ordinata)-1-i):
            if stinga_ordinata[j] > stinga_ordinata[j+1]:
                stinga_ordinata[j],stinga_ordinata[j+1] = stinga_ordinata[j+1],stinga_ordinata[j]
    return stinga_ordinata


a = "programmazione"
print("".join(sorted(a)))
