
# EX_4 SERIE_2 (révision)

def evaluer (f1, f2):
    ch = f1.readline()
    while ch != "":
        op = ch [0]
        nb1 = ch [1:ch.find(" ")]
        nb2 = ch [ch.find(" ")+1::]

        # We can use if statement :
        if op == "+" :
            result = int(nb1) + int(nb2)
        elif op == "-" :
            result = int(nb1) - int(nb2)
        elif op == "*" :
            result = int(nb1) * int(nb2)
        else :
            if int(nb2) > 0 :
                result = int(nb1) / int(nb2)
            else :
                f2.write(nb1 + op + nb2 + "=" + " error" + "\n")   

        # we can use switch case statement :
        # switch (op) :
        #     case "+" :
        #         result = int(nb1) + int(nb2)
        #     case "-" :
        #         result = int(nb1) - int(nb2)
        #     case "*" :
        #         result = int(nb1) * int(nb2)
        #     case "/" :
        #         if int(nb2) > 0 :
        #             result = int(nb1) / int(nb2)
        #         else :
        #             f2.write(nb1 + op + nb2 + "=" + " error" + "\n")

        if op != "/" and int(nb2) > 0 :
            f2.write(nb1 + op + nb2 + "=" + str(result) + "\n")
        ch = f1.readline()
    f1.close() , f2.close()



#pp
f2 = open("D:/calcul.txt", "w")
f1 = open("D:/operation.txt", "r")
evaluer(f1, f2)




