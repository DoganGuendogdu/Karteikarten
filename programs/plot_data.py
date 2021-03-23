import matplotlib.pyplot as plt
import numpy as np
import csv 

def plot_data():
    x = []
    y = []
    z = []

    with open ("files/result.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        # Ueberspringe Header
        next(csv_reader)
        
        for row in csv_reader:

            # Fuege Frage hinzu
            x.append(row[0])

            # Fuege Index der richtigen Antwort hinzu
            y.append(int(row[2]))

            #Fuege Index der falschen Antwort hinzu
            z.append(int(row[3]))

    # 'range' liefert eine Instanz von ndarray zurueck 
    # hierbei ein Array mit Dimension der Listenlaenge 
    # Abstand zwischen einzelnen Elementen ist der selbe 
    range = np.arange(len(y))
    width = 0.3 

    try:
        plt.xlabel("Frage")
        plt.ylabel("Hauefigkeiten")
        plt.title("Ergebnis des Lernens")
        plt.gcf().canvas.set_window_title("Ergebnis") # Figurenname

        plt.bar(range,      y, width, color="g")      # richtiger Index
        plt.bar(range+0.32, z, width, color="r")      # falscher Index
        plt.xticks(range, x)                          # Beschriftung X-Achse
        plt.legend(["Richtig", "Falsch"])             # Legende

        plt.show()
    except:
        print("\nFehler beim plotten der Daten")
        quit()