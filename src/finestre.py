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
        if comando == '1':
            next_window = VisualizzaCampionati()
            next_window.execute()
        elif comando == '2':
            next_window = CreaNuovoCampionato()
            next_window.execute()


class CreaNuovoCampionato(Finestra):
    def __init__(self):
        super().__init__()
        self.titolo = 'CREA NUOVO CAMPIONATO'
        self.__nome_file_campionati = 'campionati.xlsx'

    def crea_campionato(self, nome_campionato: str):
        data_creazione = pd.Timestamp.now()
        new_record = pd.DataFrame({
            'campionato': [nome_campionato],
            'data_creazione': [data_creazione]
        })
        df = utils.leggi_file_excel(self.__nome_file_campionati)
        df_campionati = pd.concat([df, new_record], ignore_index=True)
        utils.salva_file_excel(df_campionati, self.__nome_file_campionati)

    def execute(self):
        utils.stampa_titolo(self.titolo)
        nome_campionato = utils.chiedi_stringa('Nome Campionato')
        print(f'*--- Creazione campionato "{nome_campionato}" in corso...')
        conferma: bool = utils.conferma()
        if conferma:
            self.crea_campionato(nome_campionato)
            print(f'*--- Campionato "{nome_campionato}" creato con successo.')
        else:
            print("Creazione campionato annullata")


class VisualizzaCampionati(Finestra):
    def __init__(self):
        super().__init__()
        self.titolo = 'VISUALIZZA CAMPIONATI'
        self.__nome_file_campionati = 'campionati.xlsx'
        self.df_campionati = pd.DataFrame()
        self.comando_chiusura = 'E'
        self.comandi = {
            '1': 'Gestisci Campionato',
            '2': 'Elimina campionato',
            self.comando_chiusura: 'Esci'
        }

    def execute(self):
        utils.stampa_titolo(self.titolo)
        self.df_campionati = utils.leggi_file_excel(self.__nome_file_campionati)
        df = self.df_campionati.copy()
        if not df.empty:
            utils.stampa_titolo('LISTA CAMPIONATI', allineamento='<')
            df['Nome'] = df['campionato']
            df['Data creazione'] = df['data_creazione'].apply(lambda x: x.strftime('%d/%m/%Y'))
            df['Ora creazione'] = df['data_creazione'].apply(lambda x: x.strftime('%H:%M:%S'))
            print(df[['Nome', 'Data creazione', 'Ora creazione']])
        else:
            print("*--- Nessun campionato presente")
            self.comandi = {self.comando_chiusura: 'Esci'}
        while True:
            comando = self.seleziona_comando()
            if comando == self.comando_chiusura:
                break
            self.agisci(comando)
