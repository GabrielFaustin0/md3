def multiplicar(n1,n2):                                                                          
    print(n1*n2)                                                                                
def somar(n1,n2):                                                                               
    print(n1+n2)
def subtrair(n1,n2):                                                     
    print(n1-n2)
def dividir(n1,n2):
    print(n1,n2)
def menu():
    ops=0
    while ops!="5":
        print("1.mutiplicar\n2.somar\n3.subtrair\n4.dividir\n5.terminar")
        ops=input("escolha uma opção")
        if ops!="5":
            n1=float(input("digite um numero"))
            n2=float(input("digite outro numero"))
        if ops =="1":
            multiplicar(n1,n2)
        elif ops=="2":
            somar(n1,n2)
        elif ops =="3":
            subtrair(n1,n2)
        else:
            dividir(n1,n2)
def main():
    menu()
if __name__=="__main__":
    main()