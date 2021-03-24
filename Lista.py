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
  
  def inserir(self, nome, titulos, idade, cpf, posicao):
    aux = self._inicio
    no = Surfista(nome, titulos, idade, cpf)
    cont = 0

    if (posicao == 0):
      no.prox = self._inicio
      self._inicio = no
      return ''

    else:
      while ((aux.prox != None) and (cont < posicao)):
        aux = aux.prox
        cont += 1
      
      no.prox = aux.prox
      aux.prox = no
    
    self._tamanho += 1

  def remover(self, posicao):
    self._inicio = self._inicio.prox
    self._tamanho -= 1  
  
  def __str__(self):
    saida = 'Lista: ['
    p = self._inicio

    while p != None:
      saida += f'[{p.nome}, {p.titulos}, {p.idade}, {p.cpf}]'
      p = p.prox

      if p != None:
        saida += ', '
    
    saida += ']'
    return saida

  def imprimir(self):
    print(self.__str__())

  def modificar(self, novoValor):
    if self.vazia():
      raise ListaException('A Lista está vazia')
    
    self._inicio.dado = novoValor