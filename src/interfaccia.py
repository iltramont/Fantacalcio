from fantaAllenatore import FantaAllenatore
import utils

class Interfaccia:
    def __init__(self):
        pass

    def chiedi_dati_fanta_allenatore(self):
        nome_fanta_allenatore = input("Nome fanta allenatore: ")
        nome_squadra = input("Nome squadra: ")
        return nome_fanta_allenatore, nome_squadra

    def seleziona_comando(self, scelte: list[str]) -> int:
        comandi_validi = list(range(len(scelte) + 1))[1:]
        print("Selezionare operazione")
        utils.stampa_elenco_scelte(scelte)
        comando = input("Comando:")

        print("comando scelto:", comando)

    def home(self):
        scelte = [
            "Visualizza tornei",
            "Gestisci tornei"
        ]
        print("*----------------------*")
        print("*--- SCHERMATA HOME ---*")
        print("*----------------------*")
        print("Selezionare operazione")
        utils.stampa_elenco_scelte(scelte)
        scelta = input("Comando:")
        print("comando scelto:", scelta)


