import utils

class Finestra:
    def __init__(self):
        self.titolo: str | None = None
        self.descrizione: str | None = None
        self.larghezza: int = 100
        self.allineamento_titolo: str = '^'
        self.comandi: dict[str, str] | None = None

    def stampa_titolo(self):
        utils.stampa_titolo(self.titolo, self.larghezza, self.allineamento_titolo)

    def stampa_descrizione(self):
        if self.descrizione is not None:
            print(self.descrizione)

    def seleziona_comando(self) -> str:
        if self.comandi is None:
            return ''
        comandi_validi = self.comandi.keys()
        while True:
            self.stampa_titolo()
            self.stampa_descrizione()
            print("*--- Selezionare comando")
            utils.stampa_elenco_scelte(self.comandi)
            comando = input("--->").strip()
            if comando in comandi_validi:
                return comando
            else:
                print("<<<Comando non valido, riprovare>>>")

    def agisci(self, comando: str):
        pass

    def execute(self):
        comando = self.seleziona_comando()
        self.agisci(comando)



class Home(Finestra):
    def __init__(self):
        super().__init__()
        self.titolo = 'HOME'
        self.comandi = {
            '1': 'Gestisci campionati',
            '0': 'Esci'
        }

    def agisci(self, comando: str):
        if comando == '1':
            next_window = GestisciCampionati()
            next_window.execute()



class GestisciCampionati(Finestra):
    def __init__(self):
        super().__init__()
        self.titolo = 'GESTIONE CAMPIONATI'
        self.comandi = {
            '1': 'Visualizza campionati',
            '2': 'Crea nuovo campionato',
            '0': 'Esci',
        }

