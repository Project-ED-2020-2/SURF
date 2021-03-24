from Surfista import Surfista
from Campeonato import Campeonato
from Fila import FilaEncadeada, FilaException
from Lista import ListaEncadeada, ListaException
from Pilha import PilhaEncadeada, PilhaEncadeada

if __name__ == '__main__':
  p = PilhaEncadeada()
  l = ListaEncadeada()
  f = FilaEncadeada()

  l.inserir('Pedro', 1, 24, 421621, 0)
  l.inserir('Joao', 3, 20, 246115, 1)
  l.inserir('John', 2, 21, 1246242, 2)
  l.inserir('Marcos', 1, 19, 1624811, 3)
  l.inserir('Carlos', 3, 20, 236115, 4)

  print(l)