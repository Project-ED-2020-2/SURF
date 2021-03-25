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
    self._surfistasP.inserir(nome, titulos, idade, cpf)
  
  def adicionar_surfistasF(self, nome, titulos, idade, cpf):
    self._surfistasF.inserir(nome, titulos, idade, cpf)

  def buscar_surfistaCPF(self, cpf):
    return self._surfistasL.buscarCPF(cpf)
  
  def maiorIdade(self):
    return self._surfistasL.maiorIdade()
  
  def menorIdade(self):
    return self._surfistasL.menorIdade()

  def incrementaTitulo(self, cpf):
    self._surfistasL.incrementaTitulo(cpf)
  
  def remover_surfistaL(self, posicao):
    self._surfistasL.remover(posicao)
  
  def remover_surfistaF(self):
    self._surfistasF.remover()
  
  def remover_surfistaP(self):
    self._surfistasP.remover()
  
  def ordenar_surfistasL(self):
    self._surfistasL.ordenar()
  
  def imprimirSurfistasL(self):
    self._surfistasL.imprimir()
  
  def imprimirSurfistasF(self):
    self._surfistasF.imprimir()
  
  def imprimirSurfistasP(self):
    self._surfistasP.imprimir()

  def mostrar_tam_surfistasL(self):
    self._surfistasL.tamanho()
  
  def mostrar_tam_surfistasP(self):
    self._surfistasP.tamanho()
  
  def mostrar_tam_surfistasF(self):
    self._surfistasF.tamanho()
  
    