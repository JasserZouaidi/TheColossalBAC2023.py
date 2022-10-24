
# EX_2 SERIE_1 (revision)

def saisir ():
    n = int(input("n="))
    while n<2 or n>10 :
        n = int(input("n="))
    return n

def remplir (t,n) :
    for i in range (n):
        t[i]['code'] = int(input("code =")) 
        t[i]['nom'] = (input("nom =")) 
        t[i]['date_fab']['j'] = int(input("j_fab =")) 
        t[i]['date_fab']['m'] = int(input("m_fab =")) 
        t[i]['date_fab']['a'] = int(input("a_fab =")) 
        t[i]['date_exp']['j'] = int(input("j_exp =")) 
        t[i]['date_exp']['m'] = int(input("m_exp =")) 
        t[i]['date_exp']['a'] = int(input("a_exp =")) 

def expiration (t,n):
    jj = int(input("jj="))
    mm = int(input("mm="))
    aa = int(input("aa="))
    for i in range (n):
        if t[i]['date_exp']['a'] < aa :
            print(t[i]['nom'])
        elif t[i]['date_exp']['a'] == aa :
            if t[i]['date_fab']['m'] < mm :
                print(t[i]['nom'])
            elif t[i]['date_fab']['m'] == mm :
                if t[i]['date_exp']['j'] < jj :
                    print(t[i]['nom'])

#pp
from numpy import array
n = saisir()
date = {"j":int,"m":int,"a":int}
med = {"code":int,"nom":str,"date_fab":date,"date_exp":date}
t = array([med]*n)
remplir(t,n)
expiration(t,n)
