import pandas as pd
import openpyxl
from datetime import datetime
import os
import logging
from prepare import update_excel_file



path = "/home/vinpuch/Dokumente/IdeaProjects/finanzen/Daten"
filename = str(datetime.now().month) + '_' + str(datetime.now().year) + ".xlsx"

update_excel_file(path, filename)
