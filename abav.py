def ler_numero_inteiro(menssagem="introdusa um numero inteiro")->int:
    """
    Funçao que le do utilisador um nº inteiro . A função garante que o valor insserido é valido.
    """
    while True:
        dados=input(menssagem)
        if dados[0]=="-":
            testar=dados.replace("-","")
        else:
            testar=dados
        if testar.isdigit():
            return int(dados)
        print("erro:o valor não é valido")
def ler_numero_inteiro_limites(valor_min,valor_max, menssagem="introdusa um valor inteiro:")-> int:

    while True:

        dados=ler_numero_inteiro(valor_min,valor_max,"menssagem=introduza um valor")
        if dados >=valor_min and (valor_max is None or dados <= valor_max):
            return dados
        print("erro:valor nao é valido")
def ler_numero_decimal(menssagem="introdusa um numero inteiro")->int:

    """
    Funçao que le do utilisador um nº inteiro . A função garante que o valor insserido é valido.
    """
    while True:
        dados=input(menssagem)
        if len(dados)==0:
            continue
        if dados[0]=="-":
            testar=dados.replace("-","")
        else:
            testar=dados
        # sobestituir as virgulas por pontos
        testar=testar.replace(",",".")
        # contar os pontos decimais
        pontos=testar.count(".")
        #remover os pontos decimais
        testar=testar.replace(".","")
        # não pode ter mais de um ponto decimal
        if testar.isdigit() and pontos<=1:
            return float(dados)
        print("erro:o valor não é valido")
def ler_numero_decimal_limites(valormin,valormax=None,mensagem ="intruduza um valor:")->float:
    while True:
        valor=ler_numero_decimal(mensagem)
        if valor>=valormin and (valormax is None or valor<= valormax):
            return valor
        print("erro: valor não é valido")