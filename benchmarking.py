import math
from datetime import datetime
def função_complicada():
    for i in range(1000000):
        _=i**2
def função_complicada2():
    for i in range(1000000):
        _=math.pow(i,2)
def maior_tempo():
    inicio=datetime.now()
    função_complicada()
    fim=datetime.now()
    tempoex=fim-inicio
    print("tempo de execução:",tempoex.total_seconds())
maior_tempo()