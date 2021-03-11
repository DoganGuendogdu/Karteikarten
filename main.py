import datetime 
import userInput as ui
import karteikarten as kk

# Begruessung   
print()
print("Wilkommen zum Lernprogramm")
print("Bitte beachte die Gross,- und Kleinschreibung")
print("Bitte waehlen Sie ihre Csv-Datei aus")
print("Wie viele Minuten wollen Sie lernen?")



 # Aktuelle Zeit im utc Format
startTime = datetime.datetime.utcnow()

# Endzeit besteht aus der aktuellen Zeit plus der angegebenen
# Minuten, die man lernen möchte
endTime = startTime + datetime.timedelta(minutes=ui.getStudyTime())


# if datetime.datetime.utcnow() > endTime:
#     pass 
#     print("Zeitlimit ist abgelaufen!") 

# Lese die Box 1 durch den User ein
box1    = ui.getSelectedCsv()

# Checke das Format der entgegengenommenen Datei
kk.Karteikarten.checkFormatBox1(box1)


# # Karteiprogramm fuer Box 1
# print("\nBox 1")
# k1 = kk.Karteikarten(box1, box1, "files/Box_2.csv")
# k1.checkBox1()

# # Karteiprogramm fuer Box 2
# print("\nBox 2")
# k2 = kk.Karteikarten(box1, "files/Box_2.csv", "files/Box_3.csv")
# k2.checkOtherBoxes() 


# Karteiprogramm fuer Box 3
print("\nBox 3")
k3 = kk.Karteikarten(box1, "files/Box_3.csv", "files/Box_4.csv")
k3.checkOtherBoxes()

# Karteiprogramm fuer Box 4
print("\nBox 4")
k3 = kk.Karteikarten(box1, "files/Box_4.csv", "files/Box_5.csv")
k3.checkOtherBoxes()

# Karteiprogramm fuer Box 5
print("\nBox 5")
k3 = kk.Karteikarten(box1, "files/Box_5.csv", None)
k3.checkBox5()

# Gebe Statistik aus
kk.Karteikarten.getStatistics()