original="abcdefghijklmnopqrstuvwxyz"
zzcodigo="bcdefghijklmnopqrstuvwxyza"
def menu():
    op=input("Codificar.1\nDescodificar.2")
    menssagem=input("")
    if op==1:
        menssagem=codifica(menssagem)
    else:
        menssagem=descodificar(menssagem)
    print(menssagem)
def codifica(menssagem):
    global original
    global zzcodigo
    texto=""
    for l in menssagem:
        if l not in original:
            texto=texto+l
        else:
            for p in range(len(original)):
                if l ==original[p]:
                    texto=texto+zzcodigo[p]

    return texto
def descodificar(menssagem):
    global original
    global zzcodigo
    texto=""
    for l in menssagem:
        if l not in zzcodigo:
            texto=texto+l
        else:
            for p in range(len(zzcodigo)):
                if l ==zzcodigo[p]:
                    texto=texto+original[p]
    return texto
def main():
    menu()
if __name__=="__main__":
    main()