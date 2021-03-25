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
  camp1.adicionar_surfistasL('Pedro', 1, 25, 421621, 0)
  camp1.adicionar_surfistasL('Joao', 3, 20, 246115, 1)
  camp1.adicionar_surfistasL('John', 2, 21, 1246242, 2)
  camp1.adicionar_surfistasL('Marcos', 1, 19, 1624811, 3)

  camp1.adicionar_surfistasF('Carlos', 3, 22, 236115)
  camp1.adicionar_surfistasF('Artur', 1, 26, 246134)
  camp1.adicionar_surfistasF('Alan', 3, 19, 316241)
  camp1.adicionar_surfistasF('Joel', 2, 18, 624513)

  camp1.adicionar_surfistasP('Nathan', 2, 21, 246812)
  camp1.adicionar_surfistasP('Paulo', 1, 23, 624912)
  camp1.adicionar_surfistasP('Elliot', 3, 27, 126431)
  camp1.adicionar_surfistasP('Jim', 4, 25, 421983)

  #Menu

  def imprimeMenu():
        print(f'''
                        ALOHA!

        |  [1]    Cadastrar Novo Surfista     |
        |  [2]     Acrescentar Título         |
        |  [3]    Buscar Surfista por CPF     |
        |  [4]   Exibir Maior e Menor Idade   |
        |  [5]   Ordernar Surfistas Por Nome  |
        |  [6]   Exibir Surfistas Cadastrados |
        |  [7]   Mostrar Tamanho de Surfitas  |
        |  [8]       Remover um Surfista      |
        |  [9]             SAIR               |\n''')

  while True:
    imprimeMenu()
    interacao = int(input('Digite qual opção você deseja acessar: '))
    if (interacao == 1):
      nomeRecebe = input('Digite o nome do Surfista: ')
      titulosRecebe = int(input('Número de Titulos do Surfista: '))
      idadeRecebe = int(input('Idade do Surfista: '))
      cpfRecebe = int(input('CPF do Surfista: '))
      print(f'Coloque uma posição >= 0 e posição <= {camp1.mostrar_tam_surfistasL() + 1}')
      posicaoOcup = int(input('Que posição pretende ocupar na lista: '))
      camp1.adicionar_surfistasL(nomeRecebe, titulosRecebe, idadeRecebe, cpfRecebe, posicaoOcup)
      
    elif (interacao == 2):
      incrementa = input('Deseja incrementar mais um titulo? S/N').upper()
      if incrementa == 'S':
        cpfVerify = int(input('Digite o CPF do Surfista: '))
        camp1.incrementaTitulo(cpfVerify)
      
    elif (interacao == 3):
      buscaCPF = int(input('Digite o CPF do Surfista que deseja buscar: '))
      print(camp1.buscar_surfistaCPF(buscaCPF))
      
    elif (interacao == 4):
      print(camp1.menorIdade())
      print()
      print(camp1.maiorIdade())
      
    elif (interacao == 5):
      camp1.ordenar_surfistasL()
      camp1.imprimirSurfistasL()
      
    elif (interacao == 6):
      camp1.imprimirSurfistasL()
      
    elif (interacao == 7):
      print(camp1.mostrar_tam_surfistasL())
      
    elif (interacao == 8):
      remove = int(input('Digite a posição do Surfista que deseja Remover: '))
      camp1.remover_surfistaL(remove)

    else:
      break