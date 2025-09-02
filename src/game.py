from fantaAllenatore import FantaAllenatore

class Game:
    def __init__(self, numero_fanta_allenatori: int, crediti_iniziali: int, lista_fanta_allenatori: list):
        self.numero_fanta_allenatori = numero_fanta_allenatori
        self.crediti_iniziali = crediti_iniziali
        self.lista_fanta_allenatori = lista_fanta_allenatori

    def aggiungi_allenatore(self, fanta_allenatore: FantaAllenatore):
        self.lista_fanta_allenatori.append(fanta_allenatore)

