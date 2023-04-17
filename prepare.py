import os
import logging
import openpyxl
from datetime import datetime


def update_excel_file(path):
    now = datetime.now()
    month_year = now.strftime("%B_%Y")

    filename = os.path.join(path, month_year + ".xlsx")

    if os.path.exists(filename):
        db = openpyxl.load_workbook(filename)
        logging.info("Die Datei "+ filename + " wurde gefunden mit "+ month_year)
        worksheet = db.active

        for pos in worksheet.iter_rows(min_row=2, values_only=True):
            date_value = pos[0]
            # pos ist eine Zeile
            # pos[0] ist in der Zeile das erste Element
            # pos[0] ist ein datetime object welches kein Attribut row hat
            year = date_value.year
            month = date_value.month

            worksheet.cell(row=pos[0].row, column=3, value=year)
            worksheet.cell(row=pos[0].row, column=2, value=month)


        db.save(filename)
   


    else:
        raise FileNotFoundError(f"Die Datei {filename} existiert nicht.")
