import pandas as pd
import os


def read_players(file_name = "quotazioni_fantacalcio_2025_settembre.xlsx", directory = "data") -> pd.DataFrame:
    l = os.getcwd().split("\\")
    path = "\\".join(l[:len(l) - 1]) + "\\" + directory + "\\" + file_name
    return pd.read_excel(path)


def stampa_elenco_scelte(scelte: dict[str, str]):
    for key, scelta in scelte.items():
        print(f"*--- {key} = {scelta}")


def stampa_titolo(titolo: str, larghezza: int = 100, allineamento: str = '^'):
    if titolo is None:
        s = '*---' + (larghezza - 8)*'-' + '---*'
    else:
        s = f"*---{titolo:-{allineamento}{larghezza-8}}---*"
    print(s)


def chiedi_stringa(campo: str):
    while True:
        result = input(f"*--- {campo}:").strip()
        if result != '':
            return result
        else:
            print('<<< Valore nullo non consentito >>>')


def conferma() -> bool:
    while True:
        x = input("Confermare? [S / N]:").strip().upper()
        if x == 'S':
            return True
        elif x == 'N':
            return False
        else:
            print('<<< Comando non valido, valori accettati "S" / "N" >>>')


def leggi_file_excel(file_name: str) -> pd.DataFrame:
    l = os.getcwd().split("\\")
    path = "\\".join(l[:len(l) - 1]) + "\\data\\" + file_name
    if os.path.exists(path):
        return pd.read_excel(path)
    return pd.DataFrame()

def salva_file_excel(df: pd.DataFrame, file_name: str):
    l = os.getcwd().split("\\")
    path = "\\".join(l[:len(l) - 1]) + "\\data\\" + file_name
    df.to_excel(path, index=False)
