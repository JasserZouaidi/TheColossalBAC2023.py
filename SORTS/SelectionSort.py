
# SELECTIONSORT
def selectionsort(t, n):
    for i in range(n):
        pos_min = i
        for j in range(i+1, n):
            if t[j] < t[pos_min]:
                pos_min = j
        if i != pos_min:
            aux = t[i]
            t[i] = t[pos_min]
            t[pos_min] = aux

# TEST
from random import randint
from numpy import array
n = int(input('n='))
t = array([int]*n)
for i in range(n):
    t[i] = randint(1, 100)
print(t)
selectionsort(t, n)
print(t)
