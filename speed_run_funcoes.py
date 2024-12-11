# Exercício de Funções em Python
# Complete cada função conforme indicado na docstring.
from datetime import datetime
import time
def imprimir_dobro(valor):
    """Recebe um número e imprime o seu dobro."""
    print(valor*2)
valor=int(input())
imprimir_dobro(valor)
	
def calcular_media_tres_numeros(n1, n2, n3):
    """
    Calcule a média aritmética de três números.
    Retorne o valor da média.
    """
    media=(n1+n2+n3)/3
    return media
print(calcular_media_tres_numeros(10,10,10))
	
def calcular_fatorial(numero):
    """Recebe um número inteiro positivo e retorna o seu fatorial.
	    Fatorial de 5 (5!) = 5 * 4 * 3 * 2 * 1
	"""
    n=1
    numero+=1
    for i in range(1,numero):
        n=n*i
    return n
print(calcular_fatorial(5))

	
def converter_celsius_para_fahrenheit(celsius):
    """
    Converta a temperatura de Celsius para Fahrenheit.
    Fórmula: (°C × 9/5) + 32 = °F
    """
    F=(celsius*9/5)+32
    return F
print(converter_celsius_para_fahrenheit(10))
def calcular_area_circulo(raio):
    """
    Calcule a área de um círculo dado o raio.
    """
    pi = 3.14159
    area=pi*(raio**2)
    return area
print(calcular_area_circulo(5))

def exibir_contagem_regressiva(inicio):
    """Recebe um número e imprime uma contagem regressiva até 0."""
    for i in range(inicio,-1,-1):
        print(i)
        time.sleep(1)
exibir_contagem_regressiva(10)

def inverter_string(texto):
    """
    Receba uma string e retorne ela invertida.
    Exemplo: "python" -> "nohtyp"
    """
    for i in range(len(texto)-1,-1,-1 ):
        inv=inv+texto[i]
        return inv

def verificar_divisibilidade(a, b):
    """Recebe dois números e imprime se o primeiro é divisível pelo segundo."""
    if a%b == 0:
        print(a%b)
    else:
        print(None)

def calcular_perimetro_circulo(raio):
    """Recebe o raio de um círculo e retorna o seu perímetro."""
    p=2*3.14159*raio
    return p
print(calcular_perimetro_circulo(5))

def converter_segundos_para_minutos(segundos):
    """Recebe um valor em segundos e retorna o correspondente em minutos."""
    m=segundos//60
    segundosr=segundos%60
    return f"{m}:{segundosr}"
print(converter_segundos_para_minutos(30000))
def gerar_saudacao_periodo():
    """
    Retorne uma saudação baseada no período do dia.
    Se for antes de 12h: "Bom dia!"
    Entre 12h e 18h: "Boa tarde!"
    Após 18h: "Boa noite!"
    """
    hora=datetime.now().hour
    if hora>=6 and hora<12:
        print("bom dia")
    elif hora>=12 and hora<=18:
        print("boa tarde")
    else:
        print("boa noite")
gerar_saudacao_periodo()


def calcular_desconto(preco, percentual):
    """Recebe um preço e um percentual de desconto e retorna o preço com desconto."""
    percentualp=100-percentual
    d=preco*(percentualp/100)
    return d
    
def calcular_velocidade_media(distancia, tempo):
    """Recebe a distância percorrida e o tempo gasto e retorna a velocidade média."""
    v=distancia/tempo
    return v

def verificar_palindromo(palavra):
    """
    Verifique se a palavra recebida é um palíndromo.
    Palíndromo é uma palavra que pode ser lida igual de trás para frente.
    Exemplo: "radar" é um palíndromo.
    """
    inv=""
    palavra=palavra.lower()
    for i in range(len(palavra)-1,-1,-1 ):
        inv=inv+palavra[i]
    if palavra == inv:
        return True
    return False
from termcolor import colored
if verificar_palindromo("Açla"):
    print("é")
else:
    print(colored("não","red"))
def verificar_palindromov2(palavra):
    resultado=palavra==inverter_string(palavra)
    return resultado