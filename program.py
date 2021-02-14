import datetime
import random

# Begruessung
print()
print("Wilkommen zum Lernprogramm")
print("Bitte beachte die Gross,- und Kleinschreibung")
print("Wie viele Minuten wollen Sie lernen?")



# Zeiteingabe des Benutzers
eingabe = input()    
print()

# Bestimme die Lernzeit
def calculateStudyTime():

    while True:
        
        try:
            # Nehme Eingabe des Benutzers entgegen in Minuten
            # Konvertiere Eingabe in eine ganzzahlige Zahl
            input_Time = int(eingabe)

            # Wenn Eingabe negativ, so fordere zur erneuten Eingabe auf
            if input_Time < 0:
                print("Die Eingabe dar nicht negativ sein!")
                print("Geben Sie erneut eine Zahl ein")
                return calculateStudyTime()
        # Wenn Eingabe keine Zahl, so fordere zur erneuten Eingabe auf 
        except ValueError:
            print("Die Eingabe darf kein Zeichen sein.")
            print("Bitte geben Sie erneut eine Zahl ein!")
            return calculateStudyTime()

        # Aktuelle Zeit im utc Format
        startTime = datetime.datetime.utcnow()

        # Endzeit besteht aus der aktuellen Zeit plus der angegebenen 
        # Minuten, die man lernen möchte
        endTime = startTime + datetime.timedelta(minutes=input_Time)

        # Wenn die Zeit abgelaufen ist, so beende Programm
        # while True: 
        #     if (datetime.datetime.utcnow() > endTime):
        #         print("Zeitlimit ist abgelaufen!")
        #         quit()

        return input_Time        

class Karteikarten(object):

    # Leerer Konstruktor
    def __init__(self):
        pass


    # Hole zufaellige Objekte aus der Liste
    @staticmethod
    def generateRandomListObject(mylist): 
        randomObj = random.choice(mylist)
        return randomObj
    
    @staticmethod 
    def incrementFalseAnswerIndex(index): 
        indexObj = int(index)
        indexObj += 1
        str(indexObj)
        return indexObj 

    @staticmethod 
    def incrementTrueAnswerIndex(index): 
        indexObj = int(index)
        indexObj += 1
        str(indexObj)
        return indexObj 
     

    # # Loesche Elemenr aus der CSV-Datei
    # def deleteRowCSV(self, obj, filename): 
        
    #     objNew = ""


    #     for i in obj: 
            
    #         objNew += str(i)
    #         objNew += ","

    #     result = objNew[0:-1]        
    #     result[-1] = str(counter)

    #     print("result: "+ result)

    #     with open(filename, "r") as csv_delete_row: 
            
    #         for i in csv_delete_row: 
    #             print(i)



    # Lese übergebene CSV-Datei des ersten Kastens aus
    def readCsvFileBox_1(self,file): 

        # Leere Liste, der die einzelnen Daten aus der Csv Datei 
        # hinzugefuegt werden
        fragen_Antworten = []

        with open(file,"r") as csv_reader:

            # Ignoriere die einzelnen Tabellenbezeichnungen
            csv_reader.readline()

            # Lese die einzelnen Zeilen der CSV-Datei
            for line in csv_reader: 

                # Fuege die einzelnen Zeilen einer Liste hinzu.
                # Gebe an, dass die Objekte nach Kommata getrennt werden
                fragen_Antworten.append(line.split(","))

        # Gebe die Liste mit Fragen, Antworten und Fachnummer zurück
        return fragen_Antworten


     # Lese übergebene CSV-Datei aus
   
    # CSV-Reader fuer andere Boxen 
    # Unterschied: erste Zeile wird nicht uebersprungen
    def readCsvFileOtherBoxes(self,file): 

        # Leere Liste, der die einzelnen Daten aus der Csv Datei 
        # hinzugefuegt werden
        fragen_Antworten = []

        with open(file,"r") as csv_reader:

            # Lese die einzelnen Zeilen der CSV-Datei
            for line in csv_reader: 

                # Fuege die einzelnen Zeilen einer Liste hinzu.
                # Gebe an, dass die Objekte nach Kommata getrennt werden
                fragen_Antworten.append(line.split(","))

        # Gebe die Liste mit Fragen, Antworten und Fachnummer zurück
        return fragen_Antworten

    # Schreibe Listenobjekte in CSV-Datei 
    def writeCsvFile(self, obj, filename): 

        
        with open(filename, "a") as csv_writer: 
            question    = str(obj[0]) + "," 
            answer      = str(obj[1]) + ","
            answerRight = str(obj[2]) + ","
            answerWrong = str(obj[3]) + "\n"
            csv_writer.write(question+answer+answerRight+answerWrong)




        #     # # Druchlaufe die Objekte
        #     # for i in liste: 
        #     #     # Schreibe jeweiliges Objekt in Zeile
        #     #     csv_writer.write(",".join([str(j) for j in i]))
        #     #     csv_writer.write("\n")

        return csv_writer



    def checkAnswerBox_1(self, liste, writeInFile, deleteFromFile): 

        # Zaehler fuer Listeniteration    
        i = 0    

        # Durchlaufe die Liste
        while i< len(liste):
                
            # Waehle zufaelliges Objekt aus der Liste
            randomObject  = Karteikarten.generateRandomListObject(liste)

            # Index des aktuelles Elements
            indexOfCurrenObject = liste.index(randomObject)

            # Stelle Frage
            print(randomObject[0])

            # Nehme Antwort des Benutzers entgegen
            userAnswer = input()

            # Wenn die eingegebene Antwort nicht 
            # der Richtigen entspricht
            if userAnswer != randomObject[1]: 
                print("Falsche Antwort")

                # Inkrementiere den Zaheler fuer falsch-
                # beantwortete Fragen
                incrementFalseElement = Karteikarten.incrementFalseAnswerIndex(liste[indexOfCurrenObject][2])
              
                # Setze den aktuellen Zaehler fuer die falsch- 
                # beantwortete Antwort auf den inkrementierten 
                # Wert
                liste[indexOfCurrenObject][2] = incrementFalseElement

                # Durchmische die Liste
                random.shuffle(liste)

                print()
            else: 
                print("Richtige Antwort")

                # Inkrementiere den Zaheler fuer richtig-
                # beantwortete Fragen
                incrementTrueElement = Karteikarten.incrementTrueAnswerIndex(liste[indexOfCurrenObject][3])


                # Setze den aktuellen Zaehler fuer die richtig- 
                # beantwortete Antwort auf den inkrementierten 
                # Wert
                liste[indexOfCurrenObject][3] = incrementTrueElement

                # Fuege richtig-beantwortetes Objekt in die CSV-Datei
                # des nächsten Kastens
                type(self).writeCsvFile(self,randomObject,writeInFile)


                #type(self).deleteRowCSV(self, randomObject, deleteFromFile )


                # Fuege das Objekt dem zweiten Kasten hinzu 
                # und entferne es auf dem urspuenglichen Kasten
                liste.remove(randomObject)
                print()
        

    def checkOtherBoxes(self, liste, writeInFile, deleteFromFile): 
        # Zaehler fuer Listeniteration    
        i = 0    

        # Durchlaufe die Liste
        while i< len(liste):
                
            # Waehle zufaelliges Objekt aus der Liste
            randomObject  = Karteikarten.generateRandomListObject(liste)

            # Index des aktuelles Elements
            indexOfCurrenObject = liste.index(randomObject)

            # Stelle Frage
            print(randomObject[0])

            # Nehme Antwort des Benutzers entgegen
            userAnswer = input()

            # Wenn die eingegebene Antwort nicht 
            # der Richtigen entspricht
            if userAnswer != randomObject[1]: 
                print("Falsche Antwort")

                # Inkrementiere den Zaheler fuer falsch-
                # beantwortete Fragen
                incrementFalseElement = Karteikarten.incrementFalseAnswerIndex(liste[indexOfCurrenObject][2])
              
                # Setze den aktuellen Zaehler fuer die falsch- 
                # beantwortete Antwort auf den inkrementierten 
                # Wert
                liste[indexOfCurrenObject][2] = incrementFalseElement

            
                 # Fuege falsche Fragen in die Erste Box wieder ein
                type(self).writeCsvFile(self,randomObject, "Box_1.csv") 

                # Entferne die falsch beantwortete Frage aus der aktuellen Box
                liste.remove(randomObject)

                # Durchmische die Liste
                random.shuffle(liste)

                print()
            else: 
                print("Richtige Antwort")

                # Inkrementiere den Zaheler fuer richtig-
                # beantwortete Fragen
                incrementTrueElement = Karteikarten.incrementTrueAnswerIndex(liste[indexOfCurrenObject][3])


                # Setze den aktuellen Zaehler fuer die richtig- 
                # beantwortete Antwort auf den inkrementierten 
                # Wert
                liste[indexOfCurrenObject][3] = incrementTrueElement

                # Fuege richtig-beantwortetes Objekt in die CSV-Datei
                # des nächsten Kastens
                type(self).writeCsvFile(self,randomObject,writeInFile)

                # Entferne es auf dem urspuenglichen Kasten
                liste.remove(randomObject)

                # Durchmische die Liste
                random.shuffle(liste)

                #type(self).deleteRowCSV(self, randomObject, deleteFromFile )

                print()


# Lernzeit
calculateStudyTime()


# Hauptboxen
kartenBox_1 = []
kartenBox_2 = []
kartenBox_3 = []
kartenBox_4 = []
kartenBox_5 = []

box_1 = []
box_2 = []
box_3 = []
box_4 = []
box_5 = []


k1 = Karteikarten()
k2 = Karteikarten()

# Lese ersten Kasten aus 
box_1 = k1.readCsvFileBox_1("Box_1.csv")
# Lernprozess fuer den ersten Kasten
kartenbox_1 = k1.checkAnswerBox_1(box_1, "Box_2.csv", "Box_1.csv")

# ------------------------------------------------------ #
print("Moechten Sie mit der zweiten Box fortahren?")
print("ja? / nein?")
eingabe = input()
eingabe = eingabe.lower()

if eingabe == "ja": 

    # Lesen zweiten Kasten aus
    box_2 = k2.readCsvFileOtherBoxes("Box_2.csv") 
    # Lernprozess fuer den zweiten Kasten
    kartenBox_2 = k2.checkOtherBoxes(box_2, "Box_3.csv", "Box_2.csv")    

else:
    quit() 
# --------------------------------------------------- #