class Despesa:
    def __init__(self, dicionario, cor, mes):
        self._dicionario = dicionario
        self._mes = mes.title()
        self._cor = cor
    
    @property
    def dicionario(self):
        return self._dicionario

    @property
    def mes(self):
        return self._mes

    @property
    def cor(self):
        return self._cor

    def __str__(self) -> str:
        return f'Mes: {self.mes} - Valores: {self.dicionario}'