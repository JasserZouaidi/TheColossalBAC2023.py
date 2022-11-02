
# SHELLSORT
def shellsort(t, n):
    p = 0
    while p < n :
        p = 3*p+1
    while p > 0 :
        p = p // 3
        for i in range(1, n):
            x = t[i]
            j = i-1
            while j > -1 and t[j] > x:
                t[j+1] = t[j]
                j = j-1
            t[j+1] = x

# TEST
from random import randint
from numpy import array
n = int(input('n='))
t = array([int]*n)
for i in range(n):
    t[i] = randint(1, 100)
print(t)
shellsort(t, n)
print(t)
