from Surfista import Surfista
from Campeonato import Campeonato
from Fila import FilaEncadeada, FilaException
from Lista import ListaEncadeada, ListaException
from Pilha import PilhaEncadeada, PilhaEncadeada

if __name__ == '__main__':
  p = PilhaEncadeada()
  l = ListaEncadeada()
  f = FilaEncadeada()

  p.inserir('Pedro', 1, 24, 421621) # 5
  p.inserir('Joao', 3, 20, 246115) # 2
  p.inserir('John', 2, 21, 1246242) # 3
  p.inserir('Marcos', 1, 19, 1624811) # 4
  p.inserir('Carlos', 3, 20, 236115) # 1

  print()