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
    if self.vazia():
      raise ListaException('A lista está vazia.')
      
    return self._tamanho
  
  def inserir(self, nome, titulos, idade, cpf, posicao = 0):
    novo = Surfista(nome, titulos, idade, cpf)
    
    aux = self._inicio
    cont = 0

    if posicao == 0:
      novo.prox = self._inicio
      self._inicio = novo
      self._tamanho += 1
    
      return ''
    
    if aux == None:
      return ''

    else:
      while cont < posicao and aux.prox != None:
        aux = aux.prox
        cont += 1
        #if cont + 1 == posicao:

      novo.prox = aux.prox
      aux.prox = novo

      self._tamanho += 1 

      return ''
    
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