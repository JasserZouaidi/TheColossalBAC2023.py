
# EX_1 SERIE_1 (révision)

def saisir () :
    n = int(input('n='))
    while not in range(3,20) :
        n = int(input('n='))
    return n

def remplir (m,n) :
    for i in range (n) :
        for j in range (n) :
            m[i][j] = int(input('m['+str(i)+']['+str(j)+']'))
            while (m[i][j]<10 or m[i][j]>99) :
                m[i][j] = int(input('m['+str(i)+']['+str(j)+']'))

def somme (m,n) :
    s = 0
    for i in range (n) :
        for j in range (n) :
            s += m[i][j]
    return s

def dia1(m,n) :
    s = 0
    for i in range (n) :
        s += m[i][i]
    return s

def dia2(m,n) :
    s = 0
    for i in range (n) :
        s += m[i][n-i-1]
    return s

def somme_li(m,n) :
    s = 0
    for i in range (n) :
        s += m[0][i] + m[n-1][i]
    return s

def somme_col(m,n) :
    s = 0
    for i in range (n) :
        s += m[i][0] + m[i][n-1]
    return s

def remplir_fich (m,n,f) :
    f.write('--------\n')
    f.write('somme ='+str(somme(m,n))+'\n')
    f.write('dia1 ='+str(dia1(m,n))+'\n')
    f.write('dia2 ='+str(dia2(m,n))+'\n')
    f.write('somme 1ere et der li ='+str(somme_li(m,n))+'\n')
    f.write('somme 1ere et der col ='+str(somme_col(m,n))+'\n')
    f.close()



#pp
from numpy import array
n = saisir()
m = array ([[0]*n]*n)
f = open('D:\ex1.txt','w')
remplir_fich (m,n,f)
