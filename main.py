import pandas as pd
import openpyxl
from datetime import datetime
import os
import logging
from prepare import update_excel_file


now = datetime.now()
month_year = now.strftime("%B_%Y")

path = "/home/vinpuch/Dokumente/IdeaProjects/finanzen/Daten/"
filename = path + month_year + ".xlsx"

db = update_excel_file(path)

if db == None:
    ValueError("prepare ist fehlgeschlagen")