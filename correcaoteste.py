def numeroperfeto(n):
    soma=0
    for i in range(1,n):
        if n%i==0:
            soma=soma+i
    if soma==n:
        return True
    return False
def Main():
    numero=int(input("Nº:"))
    if numeroperfeto(numero)==True:
        print("numero perfeito")
    else:
        print("não é perfeito")


def calcularpreco():
    taxa=0
    


def nomedivisa(divisa):
    texto=""
    if divisa.lower=="R":
        texto="Reais [Brasil]"
    elif divisa=="D":
        texto = "Dolares"
    elif divisa=="L":
        texto=""
    else:
        texto=""
        print(texto)


def mostrartacha():
    print("Taxas:\nR->4")
def main2():
    op=input("Ver taxas S/N")
    preco=float(input("preco do produto (Euros)"))
    divisa=input("divisa(R/D/L/T)")
    if op.lower()=="S":
        mostrartacha()
    preco_covertido=calcularpreco(preco,divisa)
    print(f"preco do produto:{preco_covertido} {nomedivisa(divisa)}")