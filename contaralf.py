def contar(frase):
    for i in range(97,132):
        contar=0
        for l in frase:
            if i == ord(l):
                contar=contar+1
        print(contar)
def menu():
    frase=input("escreva uma frase")
    contar(frase)    
def main():
    menu()
if __name__=="__main__":
    main()