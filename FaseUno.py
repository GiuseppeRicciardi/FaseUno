def millecifre():
    x = 1
    y = 0
    i = 1
    while(True):
        res = x + y
        i+=1
        y = x
        x = res
        if(len(str(x)) == 1000):
            print("Il primo numero della successione di fibonacci ad avere 1000 cifre é " + str(x) + " che corrisponde "
                  "al numero in posizione " + str(i))
            break

millecifre()
