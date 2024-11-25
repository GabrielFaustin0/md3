nl=int(input("digite quantos lugares tem o avião"))
nb=int(input("digite o numero de bilhetes vendidos"))
nps=""
for i in range(nl):
    np=input("digite o numero do passageiro")
    nps=nps+np+"\n"
    nb=nb-1
    nl=nl-1
    if np=="":
        print(i)
        break
    if nb==0 or nl==0:
        break
print(nps)