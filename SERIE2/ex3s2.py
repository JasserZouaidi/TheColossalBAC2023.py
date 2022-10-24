
# EX_3 SERIE_2 (révision)

def saisir() :
    n = int(input("n="))
    while n in range(3,20) :
        n = int(input("n="))
    return n

def remplir (f,n) :
    for i in range (n) :
        x = int(input("x ="))
        while x < 0 :
            x = int(input("x ="))
        dump (x,f)
    f.close()

def affiche (f,n) :
    f = open("D:/nombre.bin","rb")
    for i in range (n) :
        x = load(f)
        print(x)
    f.close()


def somme (f,n) :
    f = open("D:/nombre.bin","rb")
    s = 0
    for i in range (n) :
        x = load (f)
        s = s + x
    print(s)
    f.close()


def minimale (f,n) :
    f = open("D:/nombre.bin","rb")
    minn = load (f)
    for i in range (n-1) :
        x = load (f)
        if minn > x :
            minn = x
    print(minn)
    f.close()


#pp
from pickle import dump,load
f = open("D:/nombre.bin","wb")
n = saisir ()
remplir (f,n)
affiche (f,n)
somme (f,n)
minimale (f,n)