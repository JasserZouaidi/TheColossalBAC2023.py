
# BUBBLESORT
def bubblesort(t, n):
    parmet = True
    while parmet == True:
        parmet = False
        for i in range(n-1):
            if t[i] > t[i+1]:
                aux = t[i]
                t[i] = t[i+1]
                t[i+1] = aux
                parmet = True
        n -= 1

# TEST
from random import randint
from numpy import array
n = int(input('n='))
t = array([int]*n)
for i in range(n):
    t[i] = randint(1, 100)
print(t)
bubblesort(t, n)
print(t)
