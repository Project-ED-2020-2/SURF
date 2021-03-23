from Surfista import Surfista

class PilhaException(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)

class PilhaEncadeada:
  def __init__(self):
    self._topo = None
    self._tamanho = 0
  
  @property
  def topo(self):
    if self.vazia():
      raise PilhaException('A pilha está vazia')

    return self._topo

  def vazia(self):
    return self._tamanho == 0
  
  def tamanho(self):
    return self._tamanho
  
  def inserir(self, nome, titulos, idade, cpf):
    no = Surfista(nome, titulos, idade, cpf)
    no.prox = self._topo
    self._topo = no

    self._tamanho += 1

  def remover(self):
    if self.vazia():
      raise PilhaException('A pilha está vazia')

    self._topo = self._topo.prox
    self._tamanho -= 1  
  
  def __str__(self):
    saida = 'Pilha: ['
    p = self._topo

    while p != None:
      saida += f'{p.dado}'
      p = p.prox

      if p != None:
        saida += ', '
    
    saida += ']'
    return saida

  def imprimir(self):
    print(self.__str__())

  def modificar(self, novoValor):
    if self.vazia():
      raise PilhaException('A pilha está vazia')
    
    self._topo.dado = novoValor