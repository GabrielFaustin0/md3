"""
Programa para calcular o vencimento de um trabalhador.
O programa deve começar por solicitar ao trabalhador que indique o seu nome, quantas horas trabalhou por dia, e quanto ganha por hora. Caso o trabalho tenho mais do que 8 horas de trabalho deve receber, por cada hora extra recebe mais 25%. Caso tenho trabalho mais do que 10 horas por dia deve receber 50% por cada hora além das 10 horas.
"""

def PedirNomeTrabalhador():
    """Esta função deve pedir o nome do trabalhador. O nome deve ter pelo menos 3 letras."""
    nome=""
    while len(nome)<3:
        nome=input("introduza um nome maior")
    return nome

def PedirHorasTrabalho():
    """Esta função pede ao utilizador quantas horas trabalho no dia. O nº de horas deve ser superior a zero."""
    horas=0
    while horas <=0:
        horas = int(input("quantas horas trabalhou"))
    return horas

def PedirOrdenado():
    """Esta função pede ao utilizado quanto ganha por cada hora de trabalho"""
    ordenado_por_hora=float(input("quanto ganha por cada hora de trabalho:"))
    return ordenado_por_hora

def MostrarVencimento(nome,horas,ordenado_por_hora):
    """Esta função deve mostrar o nome do trabalhador e quanto é que deve receber pelo dia de trabalho"""
    if horas >= 8:
        horas_n=8
    else:
        horas_n=horas
    horas_estra=horas-8
    if horas_estra > 2:
        horas_estra=2
    horas_estra_es=horas-horas_n-horas_estra
    if horas_estra < 0:
        horas_estra=0
    if horas_estra_es <0:
        horas_estra_es=0
    ordenado=(horas*ordenado_por_hora)+(horas_estra*ordenado_por_hora*1.25)+(horas_estra_es*ordenado_por_hora*1.5)
    print(f"{nome} vai receber {ordenado}€ por {horas} horas de trabalho")

def main():
    # Função principal do programa
    # pedir o nome do trabalhador
    nome=PedirNomeTrabalhador()
    # pedir as horas que trabalhou
    horas=PedirHorasTrabalho
    # pedir o ordenado por hora
    ordenado=PedirOrdenado
    # calcular e mostrar o vencimento
    MostrarVencimento(nome,horas,ordenado)

if __name__=="__main__":
    main()