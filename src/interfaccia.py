from fantaAllenatore import FantaAllenatore
import utils

class Interfaccia:
    def __init__(self):
        pass


    def chiedi_dati_fanta_allenatore(self):
        nome_fanta_allenatore = input("Nome fanta allenatore: ")
        nome_squadra = input("Nome squadra: ")
        return nome_fanta_allenatore, nome_squadra


    def seleziona_comando(self, scelte: list[str], titolo: str = "") -> int:
        comandi_validi = [str(i) for i in range(1, len(scelte) + 1)]
        result = None
        go = True
        while go:
            utils.stampa_titolo(titolo)
            print("*--- Selezionare operazione")
            utils.stampa_elenco_scelte(scelte)
            comando = input("*--- Comando:").strip()
            if comando in comandi_validi:
                result = int(comando)
                go = False
            else:
                print("<<<Comando non valido, riprovare>>>")
        return result


    def home(self):
        titolo = "SCHERMATA HOME"
        scelte = [
            "Visualizza tornei",
            "Gestisci tornei",
            "Esci"
        ]
        comando = self.seleziona_comando(scelte, titolo)
        if comando == 1:
            self.visualizza_tornei()
        elif comando == 2:
            self.gestisci_tornei()
        else:
            self.esci()


    def esci(self):
        pass


    def visualizza_tornei(self):
        pass


    def gestisci_tornei(self):
        pass
