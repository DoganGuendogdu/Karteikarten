import datetime
import random

# Begruessung
print()
print("Wilkommen zum Lernprogramm")
print("Bitte beachte die Gross,- und Kleinschreibung")
print("Wie viele Minuten wollen Sie lernen?")



# Zeiteingabe des Benutzers
eingabe = input()    

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

    liste           = []
    frage           = ""
    antwort         = ""

    # Leerer Konstruktor
    def __init__(self):
        pass
    
    # Lese übergebene CSV-Datei aus
    def readCsvFile(self,file): 
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
     


    def checkAnswer(self, liste): 

        # Zaehler fuer Listeniteration    
        i = 0    

        # Liste, in denen die richtig-beantworteten
        # Antworten stehen, also
        # der naechste Kasten
        kasten_2 = []


         # hole jede einzele Frage und speichere sie in Liste
        fragenCounter   = 0
        anwortCounter   = 0
        fehlerCounter   = 0
        richtigCounter  = 0

        # einzelne Elemente werden in einzelnen Listen verstaut
        randomObjectListe   = []
        randomQuestionList  = []
        randomAnswerList    = []
        frageListe          = []
        antwortListe        = []
        fehlerListe         = []
        richtigListe        = []


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
            else: 
                print("Richtige Antwort")

                # Inkrementiere den Zaheler fuer richtig-
                # beantwortete Fragen
                incrementTrueElement = Karteikarten.incrementTrueAnswerIndex(liste[indexOfCurrenObject][3])


                # Setze den aktuellen Zaehler fuer die richtig- 
                # beantwortete Antwort auf den inkrementierten 
                # Wert
                liste[indexOfCurrenObject][3] = incrementTrueElement

                # Fuege das Objekt dem zweiten Kasten hinzu 
                # und entferne es auf dem urspuenglichen Kasten
                kasten_2.append(randomObject)
                liste.remove(randomObject)


        print(kasten_2)
        return kasten_2







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
box_1 = k1.readCsvFile("/home/DoganFed/Documents/BauingenAufgabe/fragenAntworten.csv")
k1.checkAnswer(box_1)
