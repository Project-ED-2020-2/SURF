from Surfista import Surfista
from Campeonato import Campeonato
from Fila import FilaEncadeada, FilaException
from Lista import ListaEncadeada, ListaException
from Pilha import PilhaEncadeada, PilhaEncadeada

if __name__ == '__main__':
  p = PilhaEncadeada()
  l = ListaEncadeada()
  f = FilaEncadeada()

  camp1 = Campeonato('WSL')
  camp1.adicionar_surfistasL('Pedro', 1, 24, 421621, 0) # 5
  camp1.adicionar_surfistasL('Joao', 3, 20, 246115, 1) # 2
  camp1.adicionar_surfistasL('John', 2, 21, 1246242, 2) # 3
  camp1.adicionar_surfistasL('Marcos', 1, 19, 1624811, 3) # 4
  camp1.adicionar_surfistasL('Carlos', 3, 20, 236115, 4) # 1

  print(camp1)