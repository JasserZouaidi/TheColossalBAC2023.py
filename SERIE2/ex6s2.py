
# EX_6 SERIE_2 (révision)

def remplir_1 (ff) :
    reponse = ""
    while reponse != "N" :
        code = int(input('code ='))
        while code < 0 or len(str(code)) != 4 :
            code = int(input('code ='))
        quant = int(input('quant ='))
        while quant < 0 :
            quant = int(input('quant ='))
        prix = float(input('prix ='))
        while prix < 0 :
            prix = float(input('prix ='))
        ff.write(str(code) + " " + str(quant) + " " + str(prix))
        reponse = input ('VOULEZ VOUS CONTINUE (O/N) ?')
        while reponse not in {"N","O"} :
            reponse = input ('VOULEZ VOUS CONTINUE (O/N) ?')
    ff.close()

def remplir_2 (ff,fc) :
    ff = open ("c:/commande.txt","r")
    ch = ff.readline()
    while ch != "" :
        code = ch[0:ch.find(' ')-1]
        ch = ch [ch.find(' ')::]
        quant = ch[0:ch.find(' ')-1]
        prix = ch[ch.find(' ')+1::]
        fc.write(code + " " + str(int(quant)*int(prix)))
        ch = ff.readline()
    ff.close()
    fc.close()

def afficher (fc) :
    ch = fc.readline()
    while ch != " " :
        print (ch)
        ch = fc.readline()


#pp
ff = open ("c:/commande.txt","w")
remplir_1 (ff)
fc = open("c:/facture.txt","w")
remplir_2(ff,fc)
fc = open("c:/facture.txt","r")
afficher (fc)
