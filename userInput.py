from tkinter import *
from tkinter import filedialog


# Nehme die Lernzeit des Benutzers entgegen
def getStudyTime(): 
    # Zeiteingabe des Benutzers
    userTime = input()       
    try:
        # Nehme Eingabe des Benutzers entgegen in Minuten
        # Konvertiere Eingabe in eine ganzzahlige Zahl
        input_Time = int(userTime)

         # Wenn Eingabe negativ, so fordere zur erneuten Eingabe auf
        if input_Time < 0:
            print("Die Eingabe dar nicht negativ sein!")
            print("Geben Sie erneut eine Zahl ein")
            return getStudyTime()

    except:
        # Wenn Eingabe keine Zahl, so fordere zur erneuten Eingabe auf
        print("Die Eingabe darf kein Zeichen sein.")
        print("Bitte geben Sie erneut eine Zahl ein!")
        return getStudyTime()

    print(str(userTime)+ " Minuten")

    return input_Time

# Lese ausgewaehlte Datei des Users ein
def getSelectedCsv():
    Tk().withdraw()
    # Lese NUR CSV-Dateien ein
    file = filedialog.askopenfile(title = "Waehlen Sie eine Csv-Datei aus", filetypes = [("Csv file", ".csv")])
    
    return file