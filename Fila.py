class Node:
    def __init__(self, dado = None):
        self._dado = dado
        self._prox = None
    
    @property
    def dado(self):
        return self._dado
    
    @dado.setter
    def dado(self, novo_dado):
        self._dado = novo_dado
    
    @property
    def proximo(self):
        return self._prox
    
    @proximo.setter
    def proximo(self, novo):
        self._prox = novo


class FilaEncadeada:
    def __init__(self):
        self._inicio = None
        self._tamanho = 0