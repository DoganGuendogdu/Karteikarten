from tkinter import filedialog
import os
import tkinter
import csv



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


# Lese ausgewaehlte Datei des Users ein und
# checke auf formale Kriterien
def inputFile():

    # Root des Fensters
    root = tkinter.Tk()
    root.withdraw()

    # Entgegengenommene Datei
    file = filedialog.askopenfile(title = "Waehlen Sie eine Csv-Datei aus", filetypes = [("Csv file", ".csv")])
    
    # Liste, in der der Dateiinhalt der Csv gespeichert wird
    box = []

    try:
        # Ueberpreufe, ob Dateiinhalt leer ist
        with open(file.name) as csv_file:
            csv_reader = csv.reader(csv_file,skipinitialspace=True, delimiter = ",")

            for row in csv_reader:
                box.append(row)

        if len(box) == 0:
            print("\nDie Datei ist leer")
            print("Waehlen Sie eine andere Datei aus.")

            # Schliesse aktuelles Fenster
            root.destroy()

            return inputFile()

        else:
            # # Entferne ueberschuessige Leerzeichen 
            # with open(file.name, "r") as csv_file:
            #     csv_reader = csv.reader(csv_file, skipinitialspace=True, delimiter = ",")

            #     # for row in csv_reader:
            #     #     for e in row:
            #     hello = [x.replace(", ", "") for x in csv_reader ]
            #     print(hello)


            # Ansonsten pruefe, ob Zeilen in Datei dem erlaubten Format entspricht
            with open(file.name, "r") as csv_file:
                csv_reader = csv.reader(csv_file,skipinitialspace=True, delimiter = ",")

                for row in csv_reader:
                    
                    if len(row)<2 or len(row) > 4:
                        print("\nDie Datei entspricht NICHT dem erlaubten Format")
                        print("Waehlen Sie eine andere Datei aus.")

                        root.destroy()

                        return inputFile()



    # Exception tritt auf, wenn Dateifenster geschlossen wird
    except (AttributeError, TypeError):
        print("\nAuswahl der Datei wurde unterbrochen.")
        print("Beende Programm.")
        quit()
    # Wenn keine Fehler auftreten
    else:
        print("\nDatei wurde eingelesen.")

    root.destroy()

    return file