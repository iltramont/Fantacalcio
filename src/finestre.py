import pandas as pd

import utils

class Finestra:
    def __init__(self):
        self.titolo: str | None = None
        self.descrizione: str | None = None
        self.larghezza: int = 100
        self.allineamento_titolo: str = '^'
        self.comandi: dict[str, str] = dict()
        self.comando_chiusura: str = '0'

    def stampa_titolo(self):
        utils.stampa_titolo(self.titolo, self.larghezza, self.allineamento_titolo)

    def stampa_descrizione(self):
        if self.descrizione is not None:
            print(self.descrizione)

    def contenuto(self):
        pass

    def seleziona_comando(self) -> str:
        if self.comandi is None:
            return ''
        comandi_validi = self.comandi.keys()
        while True:
            self.stampa_titolo()
            self.stampa_descrizione()
            self.contenuto()
            print("*--- Selezionare comando")
            utils.stampa_elenco_scelte(self.comandi)
            comando = input("--->").strip()
            if comando in comandi_validi:
                return comando
            else:
                print("<<< Comando non valido, riprovare >>>")

    def agisci(self, comando: str):
        pass

    def execute(self):
        while True:
            comando = self.seleziona_comando()
            if comando == self.comando_chiusura:
                break
            self.agisci(comando)


class Home(Finestra):
    def __init__(self):
        super().__init__()
        self.titolo = 'HOME'
        self.comandi = {
            '1': 'Gestisci campionati',
            self.comando_chiusura: 'Esci'
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
            self.comando_chiusura: 'Esci'
        }

    def agisci(self, comando: str):
        if comando == '2':
            next_window = CreaNuovoCampionato()
            next_window.execute()



class CreaNuovoCampionato(Finestra):
    def __init__(self):
        super().__init__()
        self.titolo = 'CREA NUOVO CAMPIONATO'
        self.__nome_file_campionati = 'campionati.xlsx'
        self.df_campionati = pd.DataFrame()

    def crea_campionato(self, nome_campionato: str):
        data_creazione = pd.Timestamp.now()
        new_record = pd.DataFrame({
            'Campionato': [nome_campionato],
            'Data creazione': [data_creazione.strftime("%d/%m/%Y")],
            'Ora Creazione': [data_creazione.strftime("%H:%M:%S")],
        })
        df = utils.leggi_file_excel(self.__nome_file_campionati)
        df_campionati = pd.concat([df, new_record], ignore_index=True)
        utils.salva_file_excel(df_campionati, self.__nome_file_campionati)
        self.df_campionati = df_campionati


    def execute(self):
        nome_campionato = utils.chiedi_stringa('Nome Campionato')
        print(f'*--- Creazione campionato "{nome_campionato}" in corso...')
        conferma: bool = utils.conferma()
        if conferma:
            self.crea_campionato(nome_campionato)
            print(f'*--- Campionato {nome_campionato} creato con successo.')
            print('*--- Elenco campionati:')
            print(self.df_campionati)
        else:
            print("Creazione campionato annullata")
