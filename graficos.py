from matplotlib import markers
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

class Graficos():
    def __init__(self, lista_de_despesas):
        self.lista_de_despesas = lista_de_despesas
        self.exibir_grafico()
    
    def padrao_grafico(self):
        plt.title('Grafico de Despesas')
        plt.xlabel('Dias')
        plt.ylabel('Gastos em R$ (Reais)')

    def exibir_grafico(self):
        self.padrao_grafico()

        for despesa in self.lista_de_despesas:
            mLista = despesa.dicionario.items()
            cor = despesa.cor
            mes = despesa.mes
            x, y = zip(*mLista)
            plt.plot(x,y, label=mes, marker='o', markerfacecolor='blue', markersize=12, color=cor, linewidth=4)

        plt.legend()
        plt.show()

    def exibir_grafico_regressao(self, id_grafico_mes):
        despesa = self.lista_de_despesas[id_grafico_mes]
        mLista = despesa.dicionario.items()
        cor = despesa.cor
        mes = despesa.mes

        dias, valores = zip(*mLista)
        dias = np.array(dias)
        valores = np.array(valores)
        dias = dias.reshape(-1, 1)
        valores = valores.reshape(-1, 1)
        regr = LinearRegression()
        regr.fit(X=dias, y=valores)

        plt.plot(dias, regr.predict(dias), color='blue', label = "Regressão Linear")
        x, y = zip(*mLista)

        plt.plot(x, y, label = mes+str(" - original"), marker='o', markerfacecolor='olive', markersize=12, color=cor, linewidth=4)

        plt.legend()
        plt.show()
