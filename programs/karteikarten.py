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
        
        try:
            # Ausgelesene Box 
            with open(inFile, "r") as csv_file:
                csv_reader = csv.reader(csv_file)

                for line in csv_reader:
                    box.append(line)
        except FileNotFoundError:
            pass


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

        try:
            # Ausgelesene Box 
            with open(inFile, "r") as csv_file:
                csv_reader = csv.reader(csv_file)

                for line in csv_reader:
                    box.append(line)
        except FileNotFoundError:
            pass


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
        print(str(procent)+ "% der Fragen wurden richtig beantwortet\n")

    # True  --> Datei ist leer 
    # False --> Datei ist nicht leer
    def get_size_of_Csv(self,file):

        box = []

        try:
            with open(file, "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    box.append(row)
        except FileNotFoundError:
            return

        if len(box) == 0:
            return True
        else:
            return False

    # gibt Anzahl der Karten in der Csv zurueck
    def get_length_Element_Csv(self, file):
        
        box = []

        try:
            with open(file, "r") as csv_file:
                csv_reader = csv.reader(csv_file)

                for row in csv_reader:
                    box.append(row)

        except FileNotFoundError:
            return 

        return(len(box))

    # Lese die einzelnen Csv-Dateien aus,
    # um herauszufinden, wie viele Fragen
    # in den Boxen sind
    def getNumberOfQuestions(self,kasten1):

        # Box 1
        fileBox1 = kasten1.name

        # Anzahl der Karten pro Csv
        box1_length     = self.get_length_Element_Csv(fileBox1)
        box2_length     = self.get_length_Element_Csv("files/Box_2.csv")
        box3_length     = self.get_length_Element_Csv("files/Box_3.csv")
        box4_length     = self.get_length_Element_Csv("files/Box_4.csv")
        box5_length     = self.get_length_Element_Csv("files/Box_5.csv")

        print("In Box 1 sind {} Karten".format(box1_length))
        print("In Box 2 sind {} Karten".format(box2_length))
        print("In Box 3 sind {} Karten".format(box3_length))
        print("In Box 4 sind {} Karten".format(box4_length))
        print("In Box 5 sind {} Karten".format(box5_length))
        
            
    # Schaue ob alle Boxen leer sind, 
    # damit gesagt wird, dass alles beantwortet wurde
    def getFinalAnswer(self, kasten1):


        # Box 1
        fileBox1 = kasten1.name

        # Lese die Laenge alles Csv-Dateien aus
        # Wenn alle Leer, so wurde alles beantwortet
        # ausgenommen 'result.csv', die gefuellt sei muss
        box1    = self.get_size_of_Csv(fileBox1)
        box2    = self.get_size_of_Csv("files/Box_2.csv")
        box3    = self.get_size_of_Csv("files/Box_3.csv")
        box4    = self.get_size_of_Csv("files/Box_4.csv")
        box5    = self.get_size_of_Csv("files/Box_5.csv")
        result  = self.get_size_of_Csv("files/result.csv")

        if (box1 == True and box2 == True and 
            box3 == True and box4 == True and
            box5 == True and result == False):
            
            print("ALLE Fragen wurden beantwortet.\nHerzlichen Glückwunsch!")
            return True
        else:
            return False


    #-------------------------------------------------------------------------#


    #                          Exception-Handling
    #-------------------------------------------------------------------------#  
    # Uebergebe Csv, aus der gelesen wird
    # Dessen Karten alle in Box 1 anhaengen
    @staticmethod
    def write_all_cards_into_box1(box1,file):
        box = []
        try:
            # Lese die Box aus
            with open(file, "r") as csv_file:
                csv_reader = csv.reader(csv_file)

                for row in csv_reader:
                    box.append(row)
        except FileNotFoundError:
            return
        
        try:
            # Schreibe die Karten aus der ausgelesenen Box in Box1 zurueck
            write_file = box1.name
            with open(write_file, "a") as csv_file:
                csv_writer = csv.writer(csv_file)

                csv_writer.writerows(box)
        except:
            print("Fehler beim Zurueck-Hinzufuegen in Box 1")
            quit()

        # Loesche ALLE Karten aus der Csv
        open(file, "w").close()

    # Bei KeyboardInterrupt schreibe alle Karten wieder in Box 1 
    # und loesche sie aus der aktuellen Box
    def catch_KeyboardInterrupt(self,box1):
        self.write_all_cards_into_box1(box1,"files/Box_2.csv")
        self.write_all_cards_into_box1(box1,"files/Box_3.csv")
        self.write_all_cards_into_box1(box1,"files/Box_4.csv")
        self.write_all_cards_into_box1(box1,"files/Box_5.csv")
        

    #-------------------------------------------------------------------------#

