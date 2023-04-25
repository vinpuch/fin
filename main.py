import pandas as pd
import openpyxl
from datetime import datetime
import os
import logging
from prepare import update_excel_file
import sys

if sys.platform == "win" :
    path = "/home/vinpuch/Dokumente/IdeaProjects/fin/Daten"
elif sys.platform == "darwin":
    path = "/Users/vincentpuchner/Dokumente/IdeaProjects/fin/Daten"
elif sys.platform == "linux":
    path="/home/user/Dokumente/IdeaProjects/fin/Daten"





filename = str(datetime.now().month) + '_' + str(datetime.now().year) + ".xlsx"

update_excel_file(path, filename)
