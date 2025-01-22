"""Uma função que recebe uma palavra e devolve a mesma palavra convertida na lingua dos P
Alguns exemplos:
    Casa  -> Capasapa
    Bola  -> Bopolapa
    Olá   -> Opolápá
    Muito -> Muipuitopo
"""
def p(palavra):
    conssuantes="bcdfghjklmnpqrstvwxyz"
def vogal(letra):
    vogais=("aeiouáàãéèêóòõôúù")
    if letra.lower() in vogais:
        return True
    return False
def comverteemsilaba(silába):
    if vogal(silaba[0]):
        silaba =silaba + "p" +silaba.lower()
    else:
        temp="p"
        for i in range(1,len(silaba)):
            temp=temp+silaba[i]
        silaba=silaba+temp
    return silaba