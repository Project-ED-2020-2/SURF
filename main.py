from Surfista import Surfista
from Campeonato import Campeonato
from Fila import FilaEncadeada, FilaException
from Lista import ListaEncadeada, ListaException
from Pilha import PilhaEncadeada, PilhaEncadeada

if __name__ == '__main__':
  p = PilhaEncadeada()
  l = ListaEncadeada()
  f = FilaEncadeada()

  # camp1 = Campeonato('WSL')
  l.inserir('Pedro', 1, 25, 421621, 0) # 5
  l.inserir('Joao', 3, 20, 246115, 1) # 2
  l.inserir('John', 2, 21, 1246242, 2) # 3
  l.inserir('Marcos', 1, 19, 1624811, 3) # 4
  l.inserir('Carlos', 3, 22, 236115, 4) # 1

  l.remover()

  print(l)