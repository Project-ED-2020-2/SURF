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
  
  def adicionar_surfistasL(self):
    self._surfistasL.adicionar()

  def adicionar_surfistasP(self):
    self._surfistasP.adicionar()
  
  def adicionar_surfistasF(self):
    self._surfistasF.adicionar()

  def buscar_surfista(self, cpf):
    return self._surfistasL.buscar(cpf)
    