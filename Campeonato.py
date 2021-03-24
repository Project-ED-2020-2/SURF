from Lista import ListaEncadeada, ListaException
from Fila import FilaEncadeada, FilaException
from Pilha import PilhaEncadeada, PilhaEncadeada

class Campeonato:
  def __init__(self, nome_camp):
    self._nome_camp = str(nome_camp)
    self._surfistasL = ListaEncadeada()
    self._surfistasP = PilhaEncadeada()
    self._surfistasF = FilaEncadeada()

  @property
  def nome_camp(self):
    return self._nome_camp

  @nome_camp.setter
  def nome_camp(self, novo_camp):
    self._nome_camp = novo_camp
  
  def adicionar_surfistasL(self, nome, titulos, idade, cpf, posicao):
    self._surfistasL.inserir(nome, titulos, idade, cpf, posicao)

  def adicionar_surfistasP(self, nome, titulos, idade, cpf):
    self._surfistasP.adicionar(nome, titulos, idade, cpf)
  
  def adicionar_surfistasF(self, nome, titulos, idade, cpf):
    self._surfistasF.adicionar(nome, titulos, idade, cpf)

  def buscar_surfistaCPF(self, cpf):
    return self._surfistasL.buscarCPF(cpf)
  
  def buscar_surfistaPosicao(self, posicao):
    return self._surfistasL.buscarPosicao(posicao)
  
  
  # def menorIdade(self):
  #   aux = self._surfistasL.inicio
  #   menorIdade = 999

  #   while (aux.prox != None):
  #     aux = aux.prox
  #     if (aux.idade < menorIdade):
  #       menorIdade = aux
    
  #   return menorIdade
    