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

