from fantaAllenatore import FantaAllenatore
import utils

class Interfaccia:
    def __init__(self):
        pass


    def chiedi_dati_fanta_allenatore(self):
        nome_fanta_allenatore = input("Nome fanta allenatore: ")
        nome_squadra = input("Nome squadra: ")
        return nome_fanta_allenatore, nome_squadra


    def seleziona_comando(self, scelte: list[str], intestazione="") -> int:
        comandi_validi = [str(i) for i in range(1, len(scelte) + 1)]
        result = None
        go = True
        while go:
            print(intestazione)
            print("Selezionare operazione")
            utils.stampa_elenco_scelte(scelte)
            comando = input("Comando:")
            if comando in comandi_validi:
                result = int(comando)
                go = False
            else:
                print("<<<Comando non valido, riprovare>>>")
        return result


    def home(self):
        intestazione = "*----------------------*" \
                       "*--- SCHERMATA HOME ---*" \
                       "*----------------------*"
        scelte = [
            "Visualizza tornei",
            "Gestisci tornei",
            "Esci"
        ]
        scelta = self.seleziona_comando(scelte, intestazione)
        print("comando scelto:", scelta)


