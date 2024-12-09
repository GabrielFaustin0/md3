from abav import ler_numero_inteiro
from abav import ler_numero_decimal
def entrada_mesas(n_maxmesas,n_atual_m):
        
    while True:
    
        n_mesas=ler_numero_inteiro(menssagem=("quantas mesas vão ocupar"))
        if n_atual_m+n_mesas<=n_maxmesas:
            n_atual_m+=n_mesas
            print(n_atual_m)
            return n_atual_m
        else:
            print("Já não há mesas")
def entrada_clientes(n_maxclientes,n_atual_c):
    while True:
        n_clientes=ler_numero_inteiro(menssagem=("quantos lugares vão ocupar"))
        if n_atual_c+n_clientes<=n_maxclientes:
            n_atual_c+=n_clientes
            print(n_atual_c)
            return n_atual_c
        else:
            print("Já não há mais lugares desponiveis")

def saida_c(n_atual_c):
    while True:
        n_sair_c=ler_numero_inteiro(menssagem=("Quantos clêntes foram embora"))
        if n_atual_c<n_atual_c:
            n_atual_c=n_atual_c-n_sair_c
            return n_atual_c
        else:
            print("erro a mais a sair doque da")
def saida_m(n_atual_m):
    while True:
        n_sair_m=ler_numero_inteiro(menssagem=("Quantas mesas ficaram desocupadas"))
        if n_atual_m < n_sair_m:
            n_atual_m=n_atual_m-n_sair_m
            return n_atual_m
        else:
            print("É impossivel estarem mais mesas desocupadas do que aquelas que há")
def estado(n_atual_m,n_atutalc,dinero,maxclientes,maxmesas):
    b=maxmesas-n_atual_m
    print("tem",b,"mesas")
    pclientes=n_atutalc/maxclientes*100
    print("Existem",pclientes,"%","clientes")
    print("Vocé tem ",dinero,"€ no total")

def menu():
    n_maxmesas=ler_numero_inteiro(menssagem=("quantas mesas há:"))
    n_maxclientes=ler_numero_inteiro(menssagem=("digite o numero de cliêntes que o restaurante pode ocupar:"))
    op=0
    n_atual_c=0
    n_atual_m=0
    while op!="4":
        print("1.entrada\n2.saida\n3.estado\n4.terminar\n")
        op=input()
        if op=="1":
            n_atual_m=entrada_mesas(n_maxmesas,n_atual_m)
            n_atual_c=entrada_clientes(n_maxclientes,n_atual_c)
        elif op=="2":
            n_atual_c=saida_c(n_atual_c)
            n_atual_m=saida_m(n_atual_m)
            DTotal=0
            dinheirop=ler_numero_decimal("quanto pagaram")
            DTotal=DTotal+dinheirop
        else:
            estado(n_atual_m,n_atual_c,DTotal,n_maxclientes,n_maxmesas)
def main():
    menu()
if __name__=="__main__":
    main()