import csv
import random

class Karteikarten(object):

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

    # Loesche Antwort aus Kasten 1 
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

        # Zaehle Anzahl der Fragen
        # sowie richtige und falsche Antworten
        counterQuestions    = 0
        counterRightAnswer  = 0
        counterWrongAnswer  = 0
        result              = []

        i       = 0
        while(i < len(box1)):
            
            # Erhoehe den Zaehler, um herauszufinden, 
            # wie viele Fragen gestellt worden sind
            counterQuestions += 1

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
                print("Falsche Antwort")

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

        # Zaehle Anzahl der Fragen
        # sowie richtige und falsche Antworten
        counterQuestions    = 0
        counterRightAnswer  = 0
        counterWrongAnswer  = 0
        result              = []

        i       = 0
        while(i < len(box)):
            
            # Erhoehe den Zaehler, um herauszufinden, 
            # wie viele Fragen gestellt worden sind
            counterQuestions += 1

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
                print("Falsche Antwort")

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

        # Zaehle Anzahl der Fragen
        # sowie richtige und falsche Antworten
        counterQuestions    = 0
        counterRightAnswer  = 0
        counterWrongAnswer  = 0
        result              = []

        i       = 0
        while(i < len(box)):
            
            # Erhoehe den Zaehler, um herauszufinden, 
            # wie viele Fragen gestellt worden sind
            counterQuestions += 1

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

                # Entferne die richtig beantwortete Frage  
                box.remove(randomObject)

                random.shuffle(box)
                print()
            else:
                print("Falsche Antwort")

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
        