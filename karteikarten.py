import datetime
import random


class Karteikarten(object):

    # Ubergebe aktuelle CSV
    #          Kasten 1
    #          Naechster Kasten 
    def __init__(self, file, fileBefore, fileNext, resultName): 
        self._file              = file
        self._fileBefore        = fileBefore
        self._fileNext          = fileNext 
        self._resultName        = resultName

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

            # Lese die einzelnen Zeilen der CSV-Datei
            for line in csv_reader: 

                # Fuege die einzelnen Zeilen einer Liste hinzu.
                # Gebe an, dass die Objekte nach Kommata getrennt werden
                obj.append(line.split(","))

        # Liste der CSV, die aktuell ausgelesen wurde
        return obj

    # Schreibe in den naechsten Kasten
    @staticmethod
    def writeNextCsvFile(self, obj): 

        # Fuege einzelne Elemente in eine Zeile ein
        with open(self._fileNext, "a") as csv_writer: 
            question    = str(obj[0]) + "," 
            answer      = str(obj[1]) + ","
            answerRight = str(obj[2]) + ","
            answerWrong = str(obj[3])
            csv_writer.write(question+answer+answerRight+answerWrong)
            
    # Schreibe in den ersten Kasten
    def writeBeforeCsvFile(self, obj): 

        kasten1 = []   

        question    = str(obj[0]) + ","
        answer      = str(obj[1]) + ","
        answerRight = str(obj[2]) + ","
        answerWrong = str(obj[3]) 
        result      = question+answer+answerRight+answerWrong


        with open(self._fileBefore, "r") as csv_reader: 
           
            # Loesche das vorherige Element aus Kasten 1, 
            # damit Dupliakte vermieden werden
            for row in csv_reader: 
        
                kasten1.append(row)
        
        # Fuege falsch-beantwortete Frage 
        # noch dazu
        kasten1.append(result)          

        # Fuege Aktuelles Objekt in Kasten 1
        with open(self._fileBefore, "w") as csv_writer: 
            for element in kasten1: 
                csv_writer.write(element)

    # Wenn Frage in Box 1 falsch beantwortet worden ist, 
    # so muss die Csv-Datei dementsprechend geupdatet werden
    def updateFileWrongAnswersBox1(self, obj): 
        kasten1 = []   

        question    = str(obj[0]) + ","
        answer      = str(obj[1]) + ","
        answerRight = str(obj[2]) + ","
        answerWrong = str(obj[3]) 
        result      = question+answer+answerRight+answerWrong


        with open(self._file, "r") as csv_reader: 
           
            # Loesche das vorherige Element aus Kasten 1, 
            # damit Dupliakte vermieden werden
            for row in csv_reader: 
                
                # # Uerberlese die Uerbschrift
                # if "Frage" in row: 
                #     continue

                # Loesche alte Daten
                if obj[0] in row: 
                    del(row)
                else:
                    # Behalte die anderen Zeilen bei
                    kasten1.append(row)

            # Speichere neue Daten zwischen
            kasten1.append(result)

        # Fuege Neue Daten in Kasten 1
        with open(self._file, "w") as csv_writer: 
            for element in kasten1: 
                csv_writer.write(element)
        
    # Wenn Frage richtig ODER falsch beantwortet worden ist, 
    # so loesche es aus der aktuellen Box,
    # da diese in die naechste ODER vorherige uebergeht
    def deleteAnswer(self, obj): 
        
        kasten = []

        with open(self._file, "r") as csv_reader: 
            for row in csv_reader: 
                if obj[0] in row:
                    del(row)
                else: 
                    kasten.append(row)
                
        with open(self._file, "w") as csv_writer: 
            for element in kasten: 
                csv_writer.write(element)

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

    # Erhoehe Index fuer falsche Antwort
    def incrementWrongIndex(index): 
        indexObj = int(index)
        indexObj += 1
        indexObj = str(indexObj)

        if "\n" not in indexObj: 
            indexObj+="\n"

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

    # Lernprozess fuer Box 1
    def checkBox1(self,liste): 

        # Zaehler fuer Listeniteration    
        i = 0   

        # Zaehle Anzahl der Fragen
        # sowie richtige und falsche Antworten
        counterQuestions    = 0
        counterRightAnswer  = 0
        counterWrongAnswer  = 0
        result              = []

        while i< len(liste): 
            # Waehle zufaellige Frage
            randomObj = type(self).randomQuestion(liste)

            # Index des Frage-Objektes
            index     = type(self).getIndex(liste, randomObj)

            # Hole die Frage
            question  = str(type(self).getQuestion(randomObj))
            
            # Anzahl fuer korrekt-beantwortet fuer Objekt
            correctIndex = type(self).getCorrectIndex(randomObj)

            # Erhoehe den Zaehler, um herauszufinden, 
            # wie viele Fragen gestellt worden sind
            counterQuestions += 1

            # Anzahl fuer falsch-beantwortet
            falseIndex  = type(self).getWrongIndex(randomObj)

            # Stelle die Frage
            type(self).printQuestion(question)

            # Nehme Antwort des Users entgegen
            userAnswer = type(self).userAnswer()

            # Uberpruefe, ob die eingegebene Antwort
            # richtig ist
            if userAnswer == type(self).getAnswer(randomObj):
                print("Richtige Antwort!")

                # Erhoehe den Zaehler fuer die richtig-
                # beantwortete Frage fuer Objekt
                incrementTrueIndex    = type(self).incrementCorrectIndex(correctIndex)
                randomObj[2]          = incrementTrueIndex


                # Erhoehe den Zaehler, um herauszufinden, 
                # wie viele Fragen richtig beantwortet worden sind
                counterRightAnswer +=1


                # Fuege richtig-beantwortetes Objekt in die CSV-Datei
                # des zweiten Kastens
                type(self).writeNextCsvFile(self, randomObj)

                # Wenn Frage richtig, so loesche aus 
                # aktueller Csv-Datei
                type(self).deleteAnswer(self, randomObj)

                # Entferne die richtig beantwortete Frage  
                liste.remove(randomObj)

                # Durchmische die Liste
                random.shuffle(liste)

                print()
            else: 
                print("Falsche Antwort!")

                # Erhoehe den Zaehler fuer die falsch-
                # beantwortete Frage fuer Objekt
                incrementFalseIndex = type(self).incrementWrongIndex(falseIndex)
                randomObj[3]        = incrementFalseIndex

                # Erhoehe den Zaehler, um herauszufinden, 
                # wie viele Fragen falsch beantwortet worden sind
                counterWrongAnswer += 1

                # Update die Elemente in der Csv-Datei in 
                # Box 1
                type(self).updateFileWrongAnswersBox1(self,randomObj)

                print()


        # Anzahl der gestellten Fragen und 
        # richtig und falsch beatworteten 
        result  = [self._resultName, str(counterQuestions), str(counterRightAnswer), str(counterWrongAnswer)+ "\n"]
        type(self).getResultsCSV(result)
        
    # Lernprozess fuer Boxen 2 - 4
    def checkOtherBoxes(self, liste):

        # Zaehler fuer Listeniteration    
        i = 0   

        # Zaehle Anzahl der Fragen
        # sowie richtige und falsche Antworten
        counterQuestions    = 0
        counterRightAnswer  = 0
        counterWrongAnswer  = 0
        result              = []


        while i< len(liste): 
            # Waehle zufaellige Frage
            randomObj = type(self).randomQuestion(liste)

            # Index des Frage-Objektes
            index     = type(self).getIndex(liste, randomObj)

            # Hole die Frage
            question  = str(type(self).getQuestion(randomObj))
            
            # Anzahl fuer korrekt-beantwortet
            correctIndex = type(self).getCorrectIndex(randomObj)
            
            # Anzahl fuer falsch-beantwortet
            falseIndex  = type(self).getWrongIndex(randomObj)

            # Erhoehe den Zaehler, um herauszufinden, 
            # wie viele Fragen gestellt worden sind
            counterQuestions += 1

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


                # Erhoehe den Zaehler, um herauszufinden, 
                # wie viele Fragen richtig beantwortet worden sind
                counterRightAnswer +=1

                # Fuege richtig-beantwortetes Objekt in die CSV-Datei
                # des naechsten Kastens
                type(self).writeNextCsvFile(self, randomObj)

                # Wenn Frage richtig, so loesche aus 
                # aktueller Csv-Datei
                type(self).deleteAnswer(self, randomObj)

                # Entferne die richtig beantwortete Frage  
                liste.remove(randomObj)

                # Durchmische die Liste
                random.shuffle(liste)

                print()
            else: 
                print("Falsche Antwort!")

                # Erhoehe den Zaehler fuer die falsch-
                # beantwortete Frage
                incrementFalseIndex = type(self).incrementWrongIndex(falseIndex)
                randomObj[3]        = incrementFalseIndex

                # Erhoehe den Zaehler, um herauszufinden, 
                # wie viele Fragen falsch beantwortet worden sind
                counterWrongAnswer += 1

                # Schreibe falsch-beantwortete Frage in 
                # Kasten 1
                type(self).writeBeforeCsvFile(self,randomObj)

                # Loesche aktuelles Objekt aus der Liste
                type(self).deleteAnswer(self, randomObj)

                # Entferne die falsch beantwortete Frage aus der aktuellen Box
                liste.remove(randomObj)

                # Durchmische die Liste
                random.shuffle(liste)

                print()
        
        # Anzahl der gestellten Fragen und 
        # richtig und falsch beatworteten 
        result  = [self._resultName, str(counterQuestions), str(counterRightAnswer), str(counterWrongAnswer)+ "\n"]
        type(self).getResultsCSV(result)
        
    # Lernprozess fuer Box 5 
    def checkBox5(self, liste):
         # Zaehler fuer Listeniteration    
        i = 0   

        # Zaehle Anzahl der Fragen
        # sowie richtige und falsche Antworten
        counterQuestions    = 0
        counterRightAnswer  = 0
        counterWrongAnswer  = 0
        result              = []


        while i< len(liste): 
            # Waehle zufaellige Frage
            randomObj = type(self).randomQuestion(liste)

            # Index des Frage-Objektes
            index     = type(self).getIndex(liste, randomObj)

            # Hole die Frage
            question  = str(type(self).getQuestion(randomObj))
            
            # Anzahl fuer korrekt-beantwortet
            correctIndex = type(self).getCorrectIndex(randomObj)
            
            # Anzahl fuer falsch-beantwortet
            falseIndex  = type(self).getWrongIndex(randomObj)

            # Erhoehe den Zaehler, um herauszufinden, 
            # wie viele Fragen gestellt worden sind
            counterQuestions += 1

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

                 # Erhoehe den Zaehler, um herauszufinden, 
                # wie viele Fragen richtig beantwortet worden sind
                counterRightAnswer +=1


                # Wenn Frage richtig, so loesche aus 
                # aktueller Csv-Datei
                type(self).deleteAnswer(self, randomObj)

                # Entferne die richtig beantwortete Frage  
                liste.remove(randomObj)

                # Durchmische die Liste
                random.shuffle(liste)

                print()
            else: 
                print("Falsche Antwort!")

                # Erhoehe den Zaehler fuer die falsch-
                # beantwortete Frage
                incrementFalseIndex = type(self).incrementWrongIndex(falseIndex)
                randomObj[3]        = incrementFalseIndex

                # Erhoehe den Zaehler, um herauszufinden, 
                # wie viele Fragen falsch beantwortet worden sind
                counterWrongAnswer += 1

                # Schreibe falsch-beantwortete Frage in 
                # Kasten 1
                type(self).writeBeforeCsvFile(self,randomObj)

                # Loesche aktuelles Objekt aus der Liste
                type(self).deleteAnswer(self, randomObj)

                # Entferne die falsch beantwortete Frage aus der aktuellen Box
                liste.remove(randomObj)

                # Durchmische die Liste
                random.shuffle(liste)

                print()
        
        # Anzahl der gestellten Fragen und 
        # richtig und falsch beatworteten 
        result  = [self._resultName, str(counterQuestions), str(counterRightAnswer), str(counterWrongAnswer)+ "\n"]
        type(self).getResultsCSV(result)
    
    # CSV-Datei, in der die Ergebnisse stehen
    @staticmethod
    def getResultsCSV(obj): 

        result = []

        question        = str(obj[0]) + ","
        answer          = str(obj[1]) + ","
        answerRight     = str(obj[2]) + ","
        answerWrong     = str(obj[3]) 
        sumQuestions    = question+answer+answerRight+answerWrong


        with open("results.csv", "r") as csv_reader: 
           
            # Loesche das vorherige Element 
            # damit Dupliakte vermieden werden
            for row in csv_reader: 
                
                if obj[0] in row: 
                    del(row)
                else:
                    # Behalte die anderen Zeilen bei
                    result.append(row)

            # Speichere neue Daten zwischen
            result.append(sumQuestions)
              
        # Fuege Neue Daten in CSV
        with open("results.csv", "w") as csv_writer: 
            for element in result: 
                csv_writer.write(element)


# Nehme die Lernzeit des Benutzers entgegen
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


# Begruessung   
print()
print("Wilkommen zum Lernprogramm")
print("Bitte beachte die Gross,- und Kleinschreibung")
print("Wie viele Minuten wollen Sie lernen?")




 # Aktuelle Zeit im utc Format
startTime = datetime.datetime.utcnow()

# Endzeit besteht aus der aktuellen Zeit plus der angegebenen
# Minuten, die man lernen möchte
endTime = startTime + datetime.timedelta(minutes=getStudyTime())


# Listen, die die ausgelesenen Csv-Dateien darstellen
kartenBox1  = []
kartenBox2  = []
kartenBox3  = []
kartenBox4  = []
kartenBox5  = []



# if datetime.datetime.utcnow() > endTime:
    # pass 
    # print("Zeitlimit ist abgelaufen!") 

# 

# print("Box 1 jetzt")
# k1          = Karteikarten("Box_1.csv", None, "Box_2.csv", "KartenBox1")
# kartenBox1  =  k1.readCsvFileBox1()
# k1.checkBox1(kartenBox1)

# print("Box 2 jetzt")
# k2          = Karteikarten("Box_2.csv", "Box_1.csv", "Box_3.csv", "KartenBox2")
# kartenbox2  = k2.readCsvFileOtherBox() 
# k2.checkOtherBoxes(kartenbox2)

print("Box 3 jetzt")
k3          = Karteikarten("Box_3.csv", "Box_1.csv", "Box_4.csv", "KartenBox3")
kartenBox3  = k3.readCsvFileOtherBox()
k3.checkOtherBoxes(kartenBox3)

# print("Box 4 Jetzt")
# k4          = Karteikarten("Box_4.csv", "Box_1.csv", "Box_5.csv", "KartenBox4")
# kartenBox4  = k4.readCsvFileOtherBox()
# k4.checkOtherBoxes(kartenBox4)

# print("Box 5 jetzt")
# k5          = Karteikarten("Box_5.csv", "Box_1.csv", None, "KartenBox5")
# kartenBox5  = k5.readCsvFileOtherBox()
# k5.checkBox5(kartenBox5)

# print("Alle Fragen wurden beantwortet!")
# print("Hier ist ihre Statistik")
# quit()