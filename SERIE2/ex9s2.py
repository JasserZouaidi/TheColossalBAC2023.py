
# EX_9 SERIE_2 (révision)

def saisir () :
    n = int(input('n='))
    while n not in range(2,25) :
        n = int(input('n='))
    return n

def remplir_1 (m,n) :
    for i in range (n):
        for j in range (n):
            m[i][j] = input("m["+str(i)+"]["+str(j)+"]=")
        while ord(m[i][j]) not in range (65,90) :
            m[i][j] = input("m["+str(i)+"]["+str(j)+"]=")


def tst_palind (ch) :
    tst = True
    i = 0
    while tst and (len(ch)//2)>i:
        if ch[i] != ch[-i-1] :
            tst = False
        else :
            i += 1
    return tst

def remplir_2 (f,m,n) :
    for i in range (n):
        ch = ""
        for j in range (n) :
            ch += m[i][j]
        if tst_palind (ch) :
            f.write(ch+'\n')
    for i in range (n):
        ch = ""
        for j in range (n) :
            ch += m[j][i]
        if tst_palind (ch) :
            f.write(ch+'\n')
    ch = ""
    for i in range (n):
        ch += m[i][i]
    if tst_palind (ch) :
        f.write(ch+'\n')
    ch = ""
    for i in range (n-1,-1,-1) :
        ch += m[i][i]
    if tst_palind (ch) :
        f.write(ch+'\n')
    f.close()

#pp
from numpy import array
n = saisir ()
m = array([[str]*n]*n)
remplir_1(m,n)
f = open ('D:/palindrome.txt',"w")
remplir_2 (f,m,n)