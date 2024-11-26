from datetime import datetime

def tempopercorrido(h,m):
    horaatual=datetime.now().hour
    minutosatuais=datetime.now().minute
    nhora = horaatual-h
    minutos=minutosatuais-m
    if minutos<0:
        nhora-=1
        minutos=60-m+minutosatuais
    duraçaototalm=nhora*60+minutos

    return duraçaototalm
def minutos(duraçaototalm):
    blocos_15=duraçaototalm/15
    return blocos_15
def preço(p,blocos_15):
    preço=blocos_15*p
    return preço
def ler():
    h=float(input("di"))
    m=float(input("di"))
    duraçaototalm=tempopercorrido(h,m)
    m=minutos(duraçaototalm)
    p=float(input("digite quanto é pago a cada 15 minutos"))
    print("estacionamento corresponde a",round(preço(p,m),2))
def main():
    ler()
if __name__=="__main__":
    main()
