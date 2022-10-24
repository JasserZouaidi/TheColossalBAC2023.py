
# EX_10 SERIE_2 (révision)

def saisir () :
    n = int(input("n="))
    while n not in range (3,15) :
        n = int(input("n="))
    return n

def test_bin (ch) :
    tst = True
    while i<len(ch) and tst :
        if ch[i] not in {"1","0"} :
            tst = False
        else :
            i += 1
    return tst

def remplir (f,n) :
    for i in range (n) :
        ch = input ("ch =")
        while len(ch) != 4 or not(test_bin(ch)) :
            ch = input ("ch =")
    f.close()


def transfert (f,m,n) :
    f = open ("source.txt","r")
    for i in range (n) :
        ch = f.readline()
        for j in range (n) :
            m[i][j] = ch[i]
    f.close()

def reconstituer (f,m,n) :
    f = open ("source.txt","w")
    for i in range (n) :
        for j in range (n) :
            f.write(m[j][i] + "\n")
    f.close()


#pp
from numpy import array
n = saisir()
f = open("source.txt","w")
remplir(f,n)
m = array([int]*n*n)
transfert(f,m,n)
reconstituer(f,m,n)