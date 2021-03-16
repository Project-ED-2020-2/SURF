class Campeonato:
    def __init__(self, nome_camp):
        self._nome_camp = str(nome_camp)
        self._lista_Surfistas = []
        self._pilha_Surfistas = []
        self._fila_Surfistas = []
    
    @property
    def nome_camp(self):
        return self._nome_camp
    
    @nome_camp.setter
    def nome_camp(self, novo_camp):
        self._nome_camp = novo_camp
    
    # Nois que lute!!!