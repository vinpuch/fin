import os
import logging
import openpyxl
from datetime import datetime
import pandas as pd


def update_excel_file(path, filename):
    now = datetime.now()
    month_year = now.strftime("%B_%Y")

    db = pd.read_excel(path+"/"+ filename)
    logging.info("Die Datei "+ filename + " wurde gefunden mit "+ month_year)
    db["Buchnungstag"]= pd.to_datetime(db.Buchungstag)
    db.loc[(db.Buchungstag.dt.year == now.year) & (db.Buchungstag.dt.month == now.month), ["Betrag","Kontostand","Analyse-Hauptkategorie" , 
                                                                                           "Analyse-Unterkategorie"]].to_excel("./Daten/Ergebnisse/Ergebnis.xlsx")
    