class ListaEncadeada:
  def __init__(self):
    self._inicio = None
    self._tamanho = 0

  def tamanho(self):
    return self._tamanho

  def vazio(self):
    return self._tamanho == 0