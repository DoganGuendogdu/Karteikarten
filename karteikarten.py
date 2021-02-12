import datetime
import random


class Karteikarten(object):


    # Ubergebe aktuelle CSV
    #          Kasten 1
    #          Naechster Kasten 
    def __init__(self, file, fileBefore, fileNext): 
        self._file          = file
        self._fileBefore    = fileBefore
        self._fileNext      = fileNext   

    # Lese ersten Kasten aus
    # Hierbei wird Ueberschrift ignoriert
    def readCsvFileBox1(self):

        # Objekt, in dem die Fragen gespeichert werden
        obj = []   

        with open(self._file, "r") as csv_reader: 

            # Ignoriere die einzelnen Tabellenbezeichnungen
            csv_reader.readline()

            # Lese die einzelnen Zeilen der CSV-Datei
            for line in csv_reader: 

                # Fuege die einzelnen Zeilen einer Liste hinzu.
                # Gebe an, dass die Objekte nach Kommata getrennt werden
                obj.append(line.split(","))

        # Liste der CSV, die aktuell ausgelesen wurde
        return obj

    # Lese andere Kaesten aus
    # Hierbei haben diese keine Uberschrift
    def readCsvFileOtherBox(self):

        # Objekt, in dem die Fragen gespeichert werden
        obj = []   

        with open(self._file, "r") as csv_reader: 

            # Ignoriere die einzelnen Tabellenbezeichnungen
            csv_reader.readline()

            # Lese die einzelnen Zeilen der CSV-Datei
            for line in csv_reader: 

                # Fuege die einzelnen Zeilen einer Liste hinzu.
                # Gebe an, dass die Objekte nach Kommata getrennt werden
                obj.append(line.split(","))

        # Liste der CSV, die aktuell ausgelesen wurde
        return obj

    # Schreibe in den naechsten Kasten
    def writeNextCsvFile(self, liste): 

        obj = []
        # Fuege einzelne Elemente in eine Zeile ein
        with open(self._fileNext, "a") as csv_writer: 
            question    = str(liste[0]) + "," 
            answer      = str(liste[1]) + ","
            answerRight = str(liste[2]) + ","
            answerWrong = str(liste[3]) + "\n"
            csv_writer.write(question+answer+answerRight+answerWrong)

    # Schreibe in den ersten Kasten
    def writeBeforeCsvFile(self, liste): 

        obj = []
        # Fuege einzelne Elemente in eine Zeile ein
        with open(self._fileBefore, "a") as csv_writer: 
            question    = str(liste[0]) + "," 
            answer      = str(liste[1]) + ","
            answerRight = str(liste[2]) + ","
            answerWrong = str(liste[3]) + "\n"
            csv_writer.write(question+answer+answerRight+answerWrong)

    # Frage
    def getQuestion(obj):  
        
        question = obj[0]
        return str(question)

    # Stelle die Frage
    @staticmethod
    def printQuestion(question): 

        question = str(question)

        print(question)

    # Antwort des Users
    @staticmethod
    def userAnswer():
        userInput = input()
        return userInput

    # Antwort
    @staticmethod
    def getAnswer(obj): 
        answer = obj[1]
        return answer

    # Hole Index fuer richtige Antwort
    @staticmethod
    def getCorrectIndex(obj): 
        index  = obj[2]
        return int(index)

    # Erhoehe Index fuer richtige Antwort
    @staticmethod
    def incrementCorrectIndex(index): 
        indexObj = int(index)
        indexObj += 1
        str(indexObj)
        return indexObj 


    # HoleIndex fuer falsche Antwort
    @staticmethod
    def getWrongIndex(obj): 
        index  = obj[3]
        return index
    
    @staticmethod
    def getIndex(liste, obj): 
        return liste.index(obj)

    # Waehle zufaellige Frage aus der Liste
    @staticmethod
    def randomQuestion(liste): 
        obj = random.choice(liste)
        return obj


    def checkBox1(self,liste): 

        for i in liste: 
            # Waehle zufaellige Frage
            randomObj = type(self).randomQuestion(liste)

            # Index des Frage-Objektes
            index     = type(self).getIndex(liste, randomObj)

            # Hole die Frage
            question  = str(type(self).getQuestion(randomObj))
            
            # Anzahl fuer korrekt-beantwortet
            correctIndex = type(self).getCorrectIndex(randomObj)

            # Stelle die Frage
            type(self).printQuestion(question)

            # Nehme Antwort des Users entgegen
            userAnswer = type(self).userAnswer()

            # Uberpruefe, ob die eingegebene Antwort
            # richtig ist
            if userAnswer == type(self).getAnswer(randomObj):
                print("Richtige Antwort!")

                # Erhoehe den Zaehler fuer die richtig-
                # beantwortete Frage
                incrementTrueIndex    = type(self).incrementCorrectIndex(correctIndex)
                randomObj[2]          = incrementTrueIndex

                # Entferne die richtig beantwortete Frage  
                liste.remove(randomObj)

                print(liste)
                # Durchmische die Liste
                random.shuffle(liste)


# Begruessung   
print()
print("Wilkommen zum Lernprogramm")
print("Bitte beachte die Gross,- und Kleinschreibung")
print("Wie viele Minuten wollen Sie lernen?")


def getStudyTime(): 
    # Zeiteingabe des Benutzers
    userTime = input()       
    print()

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

    return input_Time


 # Aktuelle Zeit im utc Format
startTime = datetime.datetime.utcnow()

# Endzeit besteht aus der aktuellen Zeit plus der angegebenen
# Minuten, die man lernen möchte
endTime = startTime + datetime.timedelta(minutes=getStudyTime())



# while True: 
#     if datetime.datetime.utcnow() > endTime:
#         print("Zeitlimit ist abgelaufen!")
#         quit()

kartenBox1  = []

k1         = Karteikarten("Box_1.csv", None, "Box_2.csv")
kartenBox1 =  k1.readCsvFileBox1()
k1.checkBox1(kartenBox1)
