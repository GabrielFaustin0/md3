
x=int(input("intuduza o valor de x"))
y=int(input("intuduza o valor de y"))
def Quadrante(x,y):

    if x>0:
        if y >0:
            return ("1º quadrante")
        else:
            return("4º Quadrante")
    else:
        if y>0:
            return ("2º Quadrante")
        elif y<0 :
            return ("3º Quadrante")
    if x==0 or y==0:
        print("não esta nos quadrantes")

print(Quadrante(x,y))

