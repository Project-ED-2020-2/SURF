from Surfista import Surfista

class FilaException(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)

class FilaEncadeada:
  def __init__(self):
    self.__inicio = None
    self.__tamanho = 0

  @property
  def inicio(self):
    return self.__inicio

  def vazia(self):
    return self.__tamanho == 0
  
  def tamanho(self):
    return self.__tamanho
  
  def inserir(self, nome, titulos, idade, cpf):
    novo = Surfista(nome, titulos, idade, cpf)
    
    aux = self.__inicio

    if aux == None:
      self.__inicio = novo

    else:
      while aux.prox != None:
        aux = aux.prox
    
        aux.prox = novo

    self.__tamanho += 1 

  def remover(self):
    self.__inicio = self.__inicio.prox
    self.__tamanho -= 1  
  
  def __str__(self):
    saida = 'Fila: ['
    p = self.__inicio

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
      raise FilaException('A fila está vazia')
    
    self.__topo.dado = novoValor