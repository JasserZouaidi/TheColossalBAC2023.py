
# EX_8 SERIE_2 (révision)

nom1 = ""
nom2 = ""
nom3 = ""
nom4 = ""

def constriure (f1,f2,f3) :
    from pickle import dump,load
    f1 = open (nom1, "rb")
    f3 = open (nom3, "wb")
    while True :
        try :
            x = load(f1)
            f2 = open(nom2, "rb")
            dump (y,f2)
            while True :
                try :
                    y = load(f2)
                    if y%x == 0 :
                        dump (y,f3)
                except :
                    break
            f2.close()
        except :
            break
    f1.close()
    f3.close()


def gerer (f3,f4) :
    from pickle import load,dump
    from numpy import array
    t = array ([int]*1000)
    n = 0
    f3 = open (nom3 , "rb")
    f4 = open (nom4 , "wb")
    t[n] = load(f3)
    while True :
        try :
            x = load (f3)
            ok = False
            i = 0
            while not(ok) and i<=n :
                if t[i] == x :
                    ok = True
                else :
                    i += 1
            if not(ok)  :
                n += 1
                t[n] = x
        except :
            break
    f3.close()
    for i in range (n) :
        f3 = open(nom3, "rb")
        nb = 0
    while True :
        try :
            x = load (f3)
            if x==t[i] :
                nb += 1
            dump (t[i],f4)
            dump (nb,f4)
        except :
            break



