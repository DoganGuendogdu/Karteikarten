import os 
import sqlite3

                # import Modules
#----------------------------------------------#
try:
    import pandas as pd
except:
    print("Modul 'pandas' wird importiert")
    os.system('python -m pip install pandas')
#----------------------------------------------#



def createDatabase():
    # Erstelle der neuen Datenbank-Connection
    connection  = sqlite3.connect("database_file//result.db")

    cursor      = connection.cursor()

    # Erstellen der Tabelle
    cursor.execute("CREATE TABLE IF NOT EXISTS Karteikarten (Frage TEXT NOT NULL, Antwort TEXT NOT NULL, Richtig_Index INTEGER NOT NULL, Falsch_Index INTEGER NOT NULL);")
    
    # Commite SQL-Befehl
    connection.commit()

    # Csv als Pandas-DataFrame
    data = pd.read_csv("files/result.csv")
    
    # Schreibe die Daten in die Tabelle 'Karteikarten'
    # replace: Wenn Tabelle bereits existiert, so wird diese vorher gedropped und 
    # anschliessend durch die Tabelle mit den aktualisierten Daten ersetzt
    data.to_sql("Karteikarten", connection, if_exists = "replace", index = False)

    # Schliesse Connection zur Datenbank
    connection.close()