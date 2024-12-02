def somar_parametros(x,y):
    x1=0
    for i in range(x,y+1):
        x1=i+x1
    print(x1)
x=int(input("digite um numero inteiro"))
y=int(input("digite um numero inteiro"))

somar_parametros(x,y)