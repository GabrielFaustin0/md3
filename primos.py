from abav import ler_numero_inteiro
numero1=ler_numero_inteiro()
numero2=ler_numero_inteiro()

if numero1 % 2 == 0 and numero2 % 2 == 0 :
    if numero1 + 2 == numero2 or numero1 - 2 ==numero2:
        print("são primos gemios")
    else:
        print("são primos mas não gemios")
else:
    print("Não são primos")