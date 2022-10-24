
# EX_3 SERIE_1 (revision)

def remplir (f,n) :
    ch = input ('ch =')
    while ch.upper()!='FIN' :
        f.write(ch + '\n')
        ch = input ('ch =')
        n += 1
    f.close()

def afficher (f,n) :
    f = open('D:\ex3.txt','r')
    for i in range (n) :
        ch = readline (f)
        print(ch)
    f.close()

#pp
f = open('D:\ex3.txt','w')
n = 0
remplir(f,n)
afficher(f,n)
