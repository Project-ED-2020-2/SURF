from Surfista import Surfista

class ListaException(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)

class ListaEncadeada:
  def __init__(self):
    self._inicio = None
    self._tamanho = 0
  
  @property
  def inicio(self):
    return self._inicio

  def vazia(self):
    return self._tamanho == 0
  
  def tamanho(self):
    return self._tamanho
  
  def inserir(self, nome, titulos, idade, cpf):
    novo = Surfista(nome, titulos, idade, cpf)
    
    aux = self._inicio

    if aux == None:
      self._inicio = novo

    else:
      while aux.prox != None:
        aux = aux.prox
    
        aux.prox = novo

    self._tamanho += 1 

  def remover(self):
    self._inicio = self.__inicio.prox
    self._tamanho -= 1  
  
  def __str__(self):
    saida = 'Lista: ['
    p = self._inicio

    while p != None:
      saida += f'{p.nome}, {p.titulos}, {p.idade}, {p.cpf}'
      p = p.prox

      if p != None:
        saida += ', '
    
    saida += ']'
    return saida

  def imprimir(self):
    print(self.__str__())

  def modificar(self, novoValor):
    if self.vazia():
      raise ListaException('A fila está vazia')
    
    self._topo.dado = novoValor