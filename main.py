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


# Karteiprogramm fuer Box 1
k1 = kk.Karteikarten(box1, box1, "files/Box_2.csv")
k1.checkBox1()