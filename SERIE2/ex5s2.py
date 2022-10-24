
# EX_5 SERIE_2 (révision)

def test (ch) :
    tst = False
    if len(ch) == 10 :
        if ch[2] == "/" and ch[5] == "/" :
            j = ch [0:ch.find("/")]
            ch = ch [ch.find("/")+1::]
            m = ch [0:ch.find("/")]
            a = ch [ch.find("/")+1::]
            if j.isdigit() and m.isdigit() and a.isdigit() :
                if int(j) in range (1,32) and int(m) in range (1,13) and int(a) in range (1000,9999) :
                    tst = True

def remplir (f) :
    r = ""
    while r.upper()!="N" :
        livre["code"] = int(input("code ="))
        while len(str(livre["code"])) != 4 or livre["code"]<0:
            livre["code"] = int(input("code ="))
        livre["aut"] = input("aut =")
        while len(livre["aut"]) > 30 :
            livre["aut"] = input("aut =")
        livre["date_emi"] = input("dat_emi =")
        while not(test(livre["date_emi"])) :
            livre["date_emi"] = input("date_emi =")
        livre["titre"] = input("titre =")
        while len(livre["titre"]) > 20 :
            livre["titre"] = input("date_emi =")
        livre["prix"] = input("prix =")
        while int(livre["prix"]) < 0 :
            livre["prix"] = input("prix =")
        r = input("Voulez vous continuez (o/n) ?\nr=")
        while r.upper() not in {"O","N"} :
            r = input("Voulez vous continuez (o/n) ?\nr=")
        dump (livre,f)
    f.close()


def afficher_tout(f) :
    f = open("C:/4SI/livre.dat","rb")
    while True :
        try :
            l = load (f)
            print (l["code"])
            print (l["aut"])
            print (l["date_emi"])
            print (l["titre"])
            print (l["prix"])
        except :
            break
    f.close()


def afficher_un_livre(f) :
    f  = open("C:/4SI/livre.dat","rb")
    pos = int(input("pos ="))
    for i in range (pos+1) :
        l = load (f)
    print(l["code"])
    print(l["aut"])
    print(l["date_emi"])
    print(l["titre"])
    print(l["prix"])
    f.close()


def ajout_livre (f) :
    f = open("C:/4SI/livre.dat","rb")
    livre["code"] = int(input("code ="))
    while len(str(livre["code"])) != 4 or livre["code"]<0:
        livre["code"] = int(input("code ="))
    livre["aut"] = input("aut =")
    while len(livre["aut"]) > 30 :
        livre["aut"] = input("aut =")
    livre["date_emi"] = input("dat_emi =")
    while not(test(livre["date_emi"])) :
        livre["date_emi"] = input("date_emi =")
    livre["titre"] = input("titre =")
    while len(livre["titre"]) > 20 :
        livre["titre"] = input("date_emi =")
    livre["prix"] = input("prix =")
    while int(livre["prix"]) < 0 :
        livre["prix"] = input("prix =")
    dump(livre,f)
    f.close()

def transfert_en_t (f,t) :
    f = open("C:/4SI/livre.dat","rb")
    n = 0
    while True :
        try :
            l = load (f)
            t[n] = l
            n += 1
        except :
            break
    return n
    f.close()

def transfert_en_f (f,t,n) :
    f = open("C:/4SI/livre.dat","wb")
    for i in range (n) :
        dump(t[i],f)
    f.close()
        

def modif_prix (f) :
    n = transfert_en_t (f,t)
    pos = int(input("pos ="))
    n_prix = int(input("n_prix"))
    t[pos]["prix"] = n_prix
    transfert_en_f(f,t,n)

def supp_livre (f) :
    f = open ("C:/4SI/livre.dat","rb")
    n = transfert_en_t (f,t)  
    pos = int(input("pos ="))
    while pos not in range (0,n+1) :
        pos = int(input("pos="))
    for i in range (n) :
        t[i] = t[i+1]
    n -= 1
    f.close()
    transfert_en_f (f,t,n)


# pp
from pickle import dump,load
from numpy import array
f = open("C:/4SI/livre.dat","wb")
livre = {"code":int,"aut":str,"date_emi":str,"titre":str,"prix":float}
t = array([livre]*1000)
remplir(f)
choix = 0
while choix != 6 :
    print ("1-Afficher_tout\n2-Afficher_un_livre\n3-Ajout_livre\n4-Modif_livre\n5-Supp_livre\n6-Quitter\n")
    if choix == 1 :
        afficher_tout (f)
    elif choix == 2 :
        afficher_un_livre (f)
    elif choix == 3 :
        ajout_livre (f)
    elif choix == 4 :
        modif_prix (f)
    elif choix == 5 :
        supp_livre (f)
    else :
        print("FIN_PROGRAMME")