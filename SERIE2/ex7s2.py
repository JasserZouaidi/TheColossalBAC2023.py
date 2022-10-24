
# EX_7 SERIE_2 (révision)

def remplir_1 (f1) :
    ch = input("ch =")
    while ch.upper() == "FIN" :
        f1.write(ch + "\n")
        ch = input ("ch =")
    f1.close()

def netoyer (ch) :
    while ch.find("  ") != -1 :
        ch = ch[::ch.find("  ")] + ch[ch.find("  ")+1::]
    if ch[0] == " " :
        ch = ch[1::]
    if ch[-1] == " " :
        ch = ch[::-2]
    return ch

def remplir_2 (f1,f2) :
    f1 = open ("c:/texte1.txt","r")
    l = f1.readline()
    while l != "" :
        f2.write(netoyer(l) + "\n")
        l = f1.readline()
    f1.close()
    f2.close()

def inverse (ch) :
    inv = ""
    for i in range (len(ch),0) :
        inv = inv + ch[i]
    return inv

def remplir_3 (f2,f3) :
    f2 = open ("c:/texte2.txt","r")
    nb_mots = 0
    nb_lignes = 0
    l = f2.readline()
    while l != "" :
        line = l + " "
        while l.find(" ") != -1 :
            ch = l[0:ch.find(" ")]
            line = line + inverse(ch) + " "
            l = l[l.find(" ")+1::]
            nb_mots += 1
        line = line [::-2]
        f3.write(str(nb_lignes + " " + line) + "\n")
        l = f2.readline()
    f3.write(str(nb_mots))
    f2.close()
    f3.close()

# pp
f1 = open ("c:/texte1.txt","w")
remplir_1 (f1)
f2 = open ("c:/texte2.txt","w")
remplir_2 (f1,f2)
f3 = open ("c:/texte3.txt","w")
remplir_3 (f2,f3)
