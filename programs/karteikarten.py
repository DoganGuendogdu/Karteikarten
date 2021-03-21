import csv
import random

class Karteikarten(object):


    # Klassenvariablen, um Statistik zu erstellen
    # Klassenvariablen, da Instanz-unabhaengig
    counterQuestions    = 0
    counterRightAnswer  = 0
    counterWrongAnswer  = 0
    result              = []

    # Konstruktor
    def __init__(self, box1, currentBox, nextBox):
        self.__box1         = box1
        self.__currentBox   = currentBox
        self.__nextBox      = nextBox

    # Checke Format Box 1
    @classmethod
    def checkFormatBox1(cls, file):
        
        # Box1
        inFile = file.name

        # Box 2
        outFile = file.name

        # Liste, in der die einzelnen Zeilen hinterlegt sind
        lines = []


        # Lese Box 1 aus und haenge Indizes 
        # fuer richtige und falsche Antwort dran
        with open(inFile, "r") as csv_file: 
            csv_reader = csv.reader(csv_file,skipinitialspace=True, delimiter = ",")
            for row in csv_reader:
                
                # Wenn Indizes noch nicht vorhanden sind
                if len(row) == 2:
                    # Erweitere eingelesene CSV um Indizes
                    row.extend([0,0]) 
                    #Attribute jeder Zeile
                    question    = row[0]
                    answer      = row[1]
                    rightIndex  = row[2]
                    wrongIndex  = row[3]
                    # Attribute als Zeile
                    line = "{},{},{},{}\n".format(question, answer, rightIndex, wrongIndex)
                    lines.append(line)

                # Ansonsten behalte die Zeilen bei
                else:
                     #Attribute jeder Zeile
                    question    = row[0]
                    answer      = row[1]
                    rightIndex  = row[2]
                    wrongIndex  = row[3]
                    # Attribute als Zeile
                    line = "{},{},{},{}\n".format(question, answer, rightIndex, wrongIndex)
                    lines.append(line)
        
        csv_file.close()
            
        with open(outFile, "w") as csv_writer: 

            for line in lines:
                csv_writer.write(line)

        csv_writer.close()
    
    # Schreibe in den naechsten Kasten
    def writeIntoNextBox(self, obj):
        question        = obj[0]
        answer          = obj[1]
        correctIndex    = obj[2]
        falseIndex      = obj[3]   

        # Fuege einzelne Elemente in eine Zeile ein
        line = "{},{},{},{}\n".format(question, answer, correctIndex, falseIndex)

        with open(self.__nextBox, "a") as csv_writer:
            csv_writer.write(line)    

    # Schreibe Frage in Box 1, wenn diese 
    # in einer anderen Box falsch beantwortet wurde
    def writeIntoBox1(self, obj):
        
        box1 = []

        # Box 1
        file = self.__box1.name

         #Attribute jeder Zeile
        question    = obj[0]
        answer      = obj[1]
        rightIndex  = obj[2]
        wrongIndex  = obj[3]

        # Attribute als Zeile
        line = "{},{},{},{}\n".format(question, answer, rightIndex, wrongIndex)

        # Lese Box 1 aus
        with open(file, "r") as csv_reader:

            # Behalte die Fragen, die schon in Box 1 stehen, bei
            for row in csv_reader:
                box1.append(row)

        # Haenge die falsche Frage an die Datei hinzu
        box1.append(line)

        # Schreibe nun in Box 1
        with open(file, "w") as csv_writer: 
            for row in box1:
                csv_writer.write(row)

    # Wenn Frage in Box 5 richtig beantwortet wurde, 
    # schreibe diese in 'result.csv'
    def writeIntoResultCsv(self,obj):

        box              = []

        # 'result.csv'
        file = self.__nextBox

        # Attribute jeder Zeile
        question    = obj[0]
        answer      = obj[1]
        rightIndex  = obj[2]
        wrongIndex  = obj[3]

        # Attribute als Zeile
        line = "{},{},{},{}\n".format(question, answer, rightIndex, wrongIndex)

        # Header
        my_header = ["Frage","Antwort","IndexRichtig","IndexFalsch"]

        # Header als String, um beim Lesen auf einen duplikaten Header zu pruefen
        string_header = ",".join(map(str, my_header)) + "\n"


        # Fuege die richtig-beantwortete Frage hinzu
        with open(file, "a") as csv_writer:
            csv_writer.write(line)


        # Lese 'result.csv' erneut aus, damit die Frage, 
        # die als letztes beantwortet worden ist, 
        # ganz oben in der Datei steht
        with open(file, "r") as csv_reader:

            # Header wird uebersprungen
            for row in csv_reader:
                if row == string_header:
                    continue
                else:
                    box.append(row)


        # letztes Element ist nun das erste
        box.reverse()

        # Schreibe die umgedrehte Liste wieder ein
        with open(file, "w") as csv_file:
            csv_writer = csv.writer(csv_file)

            # Schreibe Header hinein
            csv_writer.writerow(i for i in my_header)

            # Schreibe einzelne Elemente hinein
            for row in box:
                csv_file.write(row)

    # Aktualsiere Fragen wenn Frage
    # in Box 1 falsch beantwortet wurde
    def updateBox1(self, obj):
        kasten = []

        file = self.__box1.name

        question        = obj[0]
        answer          = obj[1]
        correctIndex    = obj[2]
        falseIndex      = obj[3]   

        # Fuege einzelne Elemente in eine Zeile ein
        line = "{},{},{},{}\n".format(question, answer, correctIndex, falseIndex)

        # Loesche das vorherige Element aus Kasten 1, 
        # damit Dupliakte vermieden werden
        with open(file, "r") as csv_reader:
            for row in csv_reader:
                if obj[0] in row:
                    del(row) 
                    kasten.append(line)
                else:
                    # Behalte die anderen Zeilen bei
                    kasten.append(row)


        # Fuege Neue aktualisierte Daten in Kasten 1
        with open(file,"w") as csv_writer: 
            for row in kasten:
                csv_writer.write(row)

      # Checke Fragen und Antworten fuer Box 1
    
      # Loesche Antwort aus Kasten 1 
    
    # Loesche Frage aus Kasten 1
    def deleteAnswerOutBox1(self, obj):
        kasten = []

        file = self.__currentBox.name 

        with open(file, "r") as csv_reader: 
            for row in csv_reader: 
                if obj[0] in row: 
                    del(row)
                else:
                    kasten.append(row)

        with open(file, "w") as csv_writer: 
            for row in kasten:
                csv_writer.write(row)

       # Loesche Antwort aus anderen Kaesten
   
    # Loesche Fraage aus Kasten 2 - 5
    # die gleiche Methode wie von Box 1 wird hier uerberschrieben, 
    # da eingelesene Datei des Users und CSV untersch. Datentypen haben
    def deleteAnswerOutBoxes(self, obj):
        kasten = []

        file = self.__currentBox 

        with open(file, "r") as csv_reader: 
            for row in csv_reader: 
                if obj[0] in row: 
                    del(row)
                else:
                    kasten.append(row)

        with open(file, "w") as csv_writer: 
            for row in kasten:
                csv_writer.write(row)

    # Checke Fragen und Antworten fuer Box 1
    def checkBox1(self):

        box1    = []

        inFile = self.__currentBox.name

        # Ausgelesene Box 1
        with open(inFile, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                box1.append(line)


        i       = 0
        while(i < len(box1)):
            
            # Erhoehe den Zaehler, um herauszufinden, 
            # wie viele Fragen gestellt worden sind
            Karteikarten.counterQuestions += 1

            # Waehle zufaellige Frage
            randomObject = random.choice(box1)

            # Hole die Frage
            question       = randomObject[0]

            # Hole Antwort 
            answer         = randomObject[1] 

            # Anzahl fuer korrekt-beantwortet fuer Objekt
            correctIndex   = randomObject[2]

            # Anzahl fuer falsch-beantwortet
            falseIndex     = randomObject[3]

            # Stelle die Frage
            print(question)

            # Nehme Antwort des Users entgegen
            userAnswer = input()

            # Wenn Antwort richtig
            if userAnswer == answer:
                
                # Erhoehe globalen Zaehler fur richtige Frage
                Karteikarten.counterRightAnswer += 1

                print("Richtige Antwort!")

                # Erhoehe den Zaehler, um herauszufinden, 
                # wie oft die Frage richtig beantwortet wurde
                correctIndex  = int(correctIndex)
                correctIndex  += 1
                correctIndex  = str(correctIndex)

                # Aktualisiere den Index fuer korrekt-beantwortet Frage
                randomObject[2] = correctIndex

                # Wenn Frage richtig, so loesche aus aktueller Csv-Datei
                type(self).deleteAnswerOutBox1(self, randomObject)

                # Schreibe richtige Antwort in naechsten Kasten
                type(self).writeIntoNextBox(self,randomObject)

                # Entferne die richtig beantwortete Frage  
                box1.remove(randomObject)

                random.shuffle(box1)
                print()
            else:

                # Erhoehe globalen Zaehler fur falsche Frage
                Karteikarten.counterWrongAnswer += 1

                print("Falsche Antwort!")

                # Erhoehe den Zaehler, um herauszufinden, 
                # wie oft die Frage falsch beantwortet wurde
                falseIndex = int(falseIndex)
                falseIndex += 1
                falseIndex = str(falseIndex)

                # Aktualisiere den falschen Index
                randomObject[3] = falseIndex

                type(self).updateBox1(self, randomObject)

                random.shuffle(box1)
                print()

    # Checke Fragen und Antworten fuer Box 2 - 4 
    def checkOtherBoxes(self):

        box    = []

        inFile = self.__currentBox

        # Ausgelesene Box 1
        with open(inFile, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                box.append(line)


        i       = 0
        while(i < len(box)):
            
            # Erhoehe den Zaehler, um herauszufinden, 
            # wie viele Fragen gestellt worden sind
            Karteikarten.counterQuestions += 1

            # Waehle zufaellige Frage
            randomObject = random.choice(box)

            # Hole die Frage
            question       = randomObject[0]

            # Hole Antwort 
            answer         = randomObject[1] 

            # Anzahl fuer korrekt-beantwortet fuer Objekt
            correctIndex   = randomObject[2]

            # Anzahl fuer falsch-beantwortet
            falseIndex     = randomObject[3]

            # Stelle die Frage
            print(question)

            # Nehme Antwort des Users entgegen
            userAnswer = input()

            # Wenn Antwort richtig
            if userAnswer == answer:
                
                # Erhoehe globalen Zaehler fur richtige Frage
                Karteikarten.counterRightAnswer += 1

                print("Richtige Antwort!")

                # Erhoehe den Zaehler, um herauszufinden, 
                # wie oft die Frage richtig beantwortet wurde
                correctIndex  = int(correctIndex)
                correctIndex  += 1
                correctIndex  = str(correctIndex)

                # Aktualisiere den Index fuer korrekt-beantwortet Frage
                randomObject[2] = correctIndex

                # Wenn Frage richtig, so loesche aus aktueller Csv-Datei
                type(self).deleteAnswerOutBoxes(self, randomObject)

                # Schreibe richtige Antwort in naechsten Kasten
                type(self).writeIntoNextBox(self,randomObject)

                # Entferne die richtig beantwortete Frage  
                box.remove(randomObject)

                random.shuffle(box)
                print()
            else:

                # Erhoehe globalen Zaehler fur falsche Frage
                Karteikarten.counterWrongAnswer += 1

                print("Falsche Antwort!")

                # Erhoehe den Zaehler, um herauszufinden, 
                # wie oft die Frage falsch beantwortet wurde
                falseIndex = int(falseIndex)
                falseIndex += 1
                falseIndex = str(falseIndex)

                # Aktualisiere den falschen Index
                randomObject[3] = falseIndex

                # Loesche Frage aus aktueller Datei, wenn falsch
                type(self).deleteAnswerOutBoxes(self, randomObject)

                # Schreibe Frage zureuck in Box 1
                type(self).writeIntoBox1(self, randomObject)

                box.remove(randomObject)

                random.shuffle(box)
                print()
    
    # Checke Fragen und Antworten fuer Box 5
    def checkBox5(self):
        box    = []

        inFile = self.__currentBox

        # Ausgelesene Box 1
        with open(inFile, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                box.append(line)


        i       = 0
        while(i < len(box)):
            
            # Erhoehe den Zaehler, um herauszufinden, 
            # wie viele Fragen gestellt worden sind
            Karteikarten.counterQuestions += 1

            # Waehle zufaellige Frage
            randomObject = random.choice(box)

            # Hole die Frage
            question       = randomObject[0]

            # Hole Antwort 
            answer         = randomObject[1] 

            # Anzahl fuer korrekt-beantwortet fuer Objekt
            correctIndex   = randomObject[2]

            # Anzahl fuer falsch-beantwortet
            falseIndex     = randomObject[3]

            # Stelle die Frage
            print(question)

            # Nehme Antwort des Users entgegen
            userAnswer = input()

            # Wenn Antwort richtig
            if userAnswer == answer:

                # Erhoehe globalen Zaehler fur richtige Frage
                Karteikarten.counterRightAnswer += 1

                print("Richtige Antwort!")

                # Erhoehe den Zaehler, um herauszufinden, 
                # wie oft die Frage richtig beantwortet wurde
                correctIndex  = int(correctIndex)
                correctIndex  += 1
                correctIndex  = str(correctIndex)

                # Aktualisiere den Index fuer korrekt-beantwortet Frage
                randomObject[2] = correctIndex

                # Loesche Frage aus aktueller Datei, wenn falsch
                type(self).deleteAnswerOutBoxes(self, randomObject)

                # Schreibe finale richtige Antwort in 'result.csv'
                type(self).writeIntoResultCsv(self,randomObject)

                box.remove(randomObject)

                random.shuffle(box)
                print()

            else:
                #Erhoehe globalen Zaehler fur falsche Frage
                Karteikarten.counterWrongAnswer += 1

                print("Falsche Antwort!")

                # Erhoehe den Zaehler, um herauszufinden, 
                # wie oft die Frage falsch beantwortet wurde
                falseIndex = int(falseIndex)
                falseIndex += 1
                falseIndex = str(falseIndex)

                # Aktualisiere den falschen Index
                randomObject[3] = falseIndex

                # Loesche Frage aus aktueller Datei, wenn falsch
                type(self).deleteAnswerOutBoxes(self, randomObject)

                # Schreibe Frage zureuck in Box 1
                type(self).writeIntoBox1(self, randomObject)

                box.remove(randomObject)

                random.shuffle(box)
                print()
    


    #                           Statistics
    #----------------------------------------------------------------------#

    # gebe Anzahl gestellter Fragen,
    # richtig und falsch beantworteter nach jeweiliger Session aus
    def getStatisticOfQuestion(self):

        counterQuestions    = Karteikarten.counterQuestions
        counterAnswerRight  = Karteikarten.counterRightAnswer
        counterAnswerFalse  = Karteikarten.counterWrongAnswer

        # prozentuale Auswertung der Statistik
        procent = 0
        try:
            procent = counterAnswerRight/counterQuestions * 100
            procent = round(procent, 2)
        except ZeroDivisionError as AllAnswersWrong:
            print("Es wurde KEINE Frage richtig beantwortet!")
            return 0

        print("Anzahl gestellter Fragen      : "+ str(counterQuestions))
        print("Anzahl der richtigen Antworten: "+ str(counterAnswerRight))
        print("Anzahl der falschen Antworten : "+ str(counterAnswerFalse))
        print(str(procent)+ "% der Fragen wurden richtig beantwortet")
        print()

    # Methode zum Uerpruefen der Inhalte der CSV
    # wenn ALLE leer, so wurden alle Fragen beantwortet
    @staticmethod
    def get_length_of_Csv(liste):
        if len(liste) == 0:
            return True
        else:
            return False

    # Lese die einzelnen Csv-Dateien aus,
    # um herauszufinden, wie viele Fragen
    # in den Boxen sind
    def getNumberOfQuestions(self,kasten1):

        # Listen, in denen der Inhalt der einzelnen 
        # Csv Dateien gespeichert wird
        box1 = []
        box2 = []
        box3 = []
        box4 = []
        box5 = []

        # Box 1
        fileBox1 = kasten1.name

        # Lese Box 1 aus und speichere in 
        # gleichnamiger Liste
        with open(fileBox1, "r") as csv_file: 
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                box1.append(row)

            print("In Box 1 sind {} Karten".format(len(box1)))
        
        # Lese Box 2 aus und speichere in 
        # gleichnamiger Liste
        with open("files/Box_2.csv", "r") as csv_file: 
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                box2.append(row)
            
            print("In Box 2 sind {} Karten".format(len(box2)))
        
        # Lese Box 3 aus und speichere in 
        # gleichnamiger Liste
        with open("files/Box_3.csv", "r") as csv_file: 
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                box3.append(row)

            print("In Box 3 sind {} Karten".format(len(box3)))
        
        # Lese Box 4 aus und speichere in 
        # gleichnamiger Liste
        with open("files/Box_4.csv", "r") as csv_file: 
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                box4.append(row)

            print("In Box 4 sind {} Karten".format(len(box4)))

        # Lese Box 5 aus und speichere in 
        # gleichnamiger Liste
        with open("files/Box_5.csv", "r") as csv_file: 
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                box5.append(row)

            print("In Box 5 sind {} Karten".format(len(box5)))

    # Schaue ob alle Boxen leer sind, 
    # damit gesagt wird, dass alles beantwortet wurde
    def getFinalAnswer(self, kasten1):
        # Listen, in denen der Inhalt der einzelnen 
        # Csv Dateien gespeichert wird
        box1    = []
        box2    = []
        box3    = []
        box4    = []
        box5    = []
        result  = []

        # Box 1
        fileBox1 = kasten1.name

        # Lese Box 1 aus und speichere in 
        # gleichnamiger Liste
        with open(fileBox1, "r") as csv_file: 
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                box1.append(row)

        # Lese Box 2 aus und speichere in 
        # gleichnamiger Liste
        with open("files/Box_2.csv", "r") as csv_file: 
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                box2.append(row)
            
        # Lese Box 3 aus und speichere in 
        # gleichnamiger Liste
        with open("files/Box_3.csv", "r") as csv_file: 
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                box3.append(row)
        
        # Lese Box 4 aus und speichere in 
        # gleichnamiger Liste
        with open("files/Box_4.csv", "r") as csv_file: 
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                box4.append(row)

        # Lese Box 5 aus und speichere in 
        # gleichnamiger Liste
        with open("files/Box_5.csv", "r") as csv_file: 
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                box5.append(row)


        # Ueberpruefe, ob ALLE Dateien leer sind    
        b1 = self.get_length_of_Csv(box1)
        b2 = self.get_length_of_Csv(box2)
        b3 = self.get_length_of_Csv(box3)
        b4 = self.get_length_of_Csv(box4)
        b5 = self.get_length_of_Csv(box5)
        
        if (b1 == True and b2 == True and 
            b3 == True and b4 == True and
            b5 == True):
            
            print("ALLE Fragen wurden beantwortet.\nHerzlichen Glückwunsch!")
            return True
        else:
            return False