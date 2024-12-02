def letras_iguais(texto):
    for i in texto:
        if i!=texto[0]:
            return False
    return True
texto=(input("digite um numero inteiro"))
print(letras_iguais(texto))