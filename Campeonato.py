from Lista import ListaEncadeada, ListaException
from Fila import FilaEncadeada, FilaException
from Pilha import PilhaEncadeada, PilhaEncadeada

class Campeonato:
  def __init__(self, nome_camp):
    self._nome_camp = str(nome_camp)
    self._lista_Surfistas = ListaEncadeada()
    self._pilha_Surfistas = PilhaEncadeada()
    self._fila_Surfistas = FilaEncadeada()

  @property
  def nome_camp(self):
    return self._nome_camp

  @nome_camp.setter
  def nome_camp(self, novo_camp):
    self._nome_camp = novo_camp
    