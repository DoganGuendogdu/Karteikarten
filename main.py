import datetime 
import os
import sys
import programs.userInput    as ui
import programs.karteikarten as kk
import programs.database     as db


def main():

                        # Lernprogramm
#-----------------------------------------------------------------------------#
    # Begruessung   
    print("\nWilkommen zum Lernprogramm")
    print("Bitte beachte die Gross,- und Kleinschreibung")
    print("Bitte waehlen Sie ihre Csv-Datei aus")
    
    # Lese die Box 1 durch den User ein und checke auf Fehler
    box1    = ui.inputFile()
    
    # Checke das Format der entgegengenommenen Datei
    kk.Karteikarten.checkFormatBox1(box1)
    
    # print("\nWie viele Minuten wollen Sie lernen?")
    
     # Aktuelle Zeit im utc Format
    # startTime = datetime.datetime.utcnow()
    
    # Endzeit besteht aus der aktuellen Zeit plus der angegebenen
    # Minuten, die man lernen möchte
    # endTime = startTime + datetime.timedelta(minutes=ui.getStudyTime())
    
    
    # if datetime.datetime.utcnow() > endTime:
    #     pass 
    #     print("Zeitlimit ist abgelaufen!") 
    
    
    # # Karteiprogramm fuer Box 1
    print("\nBox 1")
    k1 = kk.Karteikarten(box1, box1, "files/Box_2.csv")
    k1.checkBox1()
    
    # # Karteiprogramm fuer Box 2
    print("\nBox 2")
    k2 = kk.Karteikarten(box1, "files/Box_2.csv", "files/Box_3.csv")
    k2.checkOtherBoxes() 
    
    # # Karteiprogramm fuer Box 3
    print("\nBox 3")
    k3 = kk.Karteikarten(box1, "files/Box_3.csv", "files/Box_4.csv")
    k3.checkOtherBoxes()

    # Karteiprogramm fuer Box 4
    print("\nBox 4")
    k4 = kk.Karteikarten(box1, "files/Box_4.csv", "files/Box_5.csv")
    k4.checkOtherBoxes()

    # Karteiprogramm fuer Box 5
    print("\nBox 5")
    k5 = kk.Karteikarten(box1, "files/Box_5.csv", "files/result.csv")
    k5.checkBox5()
#-----------------------------------------------------------------------------#



                        # Statistik
#-------------------------------------------------------------------------#
    r = kk.Karteikarten(None,None,None)
    # Gebe Statistik ueber gestelle Fragen aus
    r.getStatisticOfQuestion()
    # Gebe aus, wie viele Fragen noch in den Boxen
    r.getNumberOfQuestions(box1)
    # schaue, ob alle Fragen beantwortet wurden
    final_answer = r.getFinalAnswer(box1)
#-------------------------------------------------------------------------#



                       # Datenbank
#----------------------------------------------------------------------------#
    # Wenn alle richtig Fragen beantwortet worden sind, 
    # erstelle Datenbank
    if final_answer == True:
        db.createDatabase()
        print("\nCreated Database!")
        print("Die Datenbank ist im Ornder 'database_file' zu finden")
#----------------------------------------------------------------------------#



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgramm wurde beendet.")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)