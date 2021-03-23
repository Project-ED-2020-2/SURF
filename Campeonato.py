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

  # @property
  # def surfistasL(self):
  #   return self._lista_Surfistas

  # @surfistasL.setter
  # def surfistasL(self):
  #   self._lista_Surfistas.inserir()

  # @property
  # def surfistasP(self):
  #   return self._pilha_Surfistas

  # @surfistasP.setter
  # def surfistasP(self, surfistasP):
  #   self._pilha_Surfistas = surfistasP

  # @property
  # def surfistasF(self):
  #   return self._fila_Surfistas

  # @surfistasF.setter
  # def surfistasF(self, surfistasF):
  #   self._fila_Surfistas = surfistasF

  # def menor_idade(self):
  #   idade_min = 99
  #   for i in range(len(self._lista_Surfistas)):
  #     if (self._lista_Surfistas[i].idade < idade_min):
  #       idade_min = (self._lista_Surfistas[i].idade)
    
  #   return idade_min

  # def maior_idade(self):


# Nois que lute!!!