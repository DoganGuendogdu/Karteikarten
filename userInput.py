from tkinter import *
from tkinter import filedialog

# Lese ausgewaehlte Datei des Users ein
def getSelectedCsv():
    Tk().withdraw()
    # Lese NUR CSV-Dateien ein
    file = filedialog.askopenfile(title = "Waehlen Sie eine Csv-Datei aus", filetypes = [("Csv file", ".csv")])
   
    return file