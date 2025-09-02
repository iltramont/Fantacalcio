import pandas as pd
import os


def read_players(file_name = "quotazioni_fantacalcio_2025_settembre.xlsx", directory = "data") -> pd.DataFrame:
    l = os.getcwd().split("\\")
    path = "\\".join(l[:len(l) - 1]) + "\\" + directory + "\\" + file_name
    return pd.read_excel(path)


def stampa_elenco_scelte(scelte: list):
    for i, scelta in enumerate(scelte):
        print(f"{i + 1} = {scelta}")
