import datetime
dia=int(input("dia"))
mes=int(input("mes"))
ano=int(input("ano"))
hoje=datetime.date.today
datan=datetime.date(ano,mes,dia)
idade=hoje.year-datan.year
if datan.month>hoje.month(datan.month==hoje.month and datan.day>hoje.py):
    idade-=1
print(idade)