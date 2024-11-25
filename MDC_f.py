def MDC(n1,n2):
    menor = n1
    if n2<menor:
        menor=2
    md=None
    for i in range(2,menor):
        if n1%i==0 and n2%i==0:
            print(i)
n1=input("digite o numero do passageiro")
n2=input("digite o numero do passageiro")
MDC(n1,n2)