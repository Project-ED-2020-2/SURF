from Surfista import Surfista
from Campeonato import Campeonato
from Fila import FilaEncadeada, FilaException
from Lista import ListaEncadeada, ListaException
from Pilha import PilhaEncadeada, PilhaEncadeada

if __name__ == '__main__':
  p = PilhaEncadeada()
  l = ListaEncadeada()
  f = FilaEncadeada()

  f.inserir('Pedro', 1, 24, 421621)
  l.inserir('Joao', 3, 20, 246115)
  p.inserir('John', 2, 21, 1246242)
  p.inserir('Marcos', 1, 19, 1624811)

  print(f)
  print(l)
  print(p)
