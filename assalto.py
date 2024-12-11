import math
def pdirvalorsaque():
    valor_saque=0
    while valor_saque > 0:
        valor_saque=float(input("de quanto fpoi o saque"))
    return valor_saque
def dividir_dinero(valor_saque):
    valorlider=round(valor_saque/2,2)
    print(f"O lider leva {valorlider}")
    valor_dos2=round(valor_saque*0.20,2)
    print(f"os dois levam{valor_dos2}")
    condutor=round(valor_saque*0.10,2)
    print(f"o condutor leva{condutor}")
    nsuspeitas(valorlider)
    nsuspeitas(valor_dos2)
    nsuspeitas(condutor)
def nsuspeitas(valor):
    valor_m=valor*0.05
    if valor_m>1000:
        valor_m=1000
    meses=valor/valor_m
    meses=math.ceil(meses)
    print(f"os{valor}€ são gastos em {meses} meses, gastando {valor_m}€ por mês.")

def main():
    valor=pdirvalorsaque()
    dividir_dinero(valor)


if __name__=="__main__":
    main()