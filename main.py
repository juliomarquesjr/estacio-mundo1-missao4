from despesas import Despesa
from graficos import Graficos

#Despesas por mes
maio = Despesa({1:100, 2:90, 5:80, 6:100, 10:80, 20:120}, 'red', 'maio')
junho = Despesa({1:100, 2:120, 5:150, 6:140, 12:120,20:100, 22:90}, 'skyblue', 'junho')
julho = Despesa({1:95, 2:130, 5:155, 6:110, 10:90, 20:110, 22:120}, 'olive', 'julho')
#agosto = Despesa({1:400, 2:310, 5:60, 9:19, 10:210, 20:600, 22:20}, 'olive', 'agosto')

lista_meses = [maio, junho, julho]

grafico = Graficos(lista_meses)
grafico.exibir_grafico_regressao(0)

