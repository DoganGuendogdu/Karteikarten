import datetime 
import sys
import programs.userInput    as ui
import programs.karteikarten as kk
import programs.database     as db
import programs.plot_data    as plot


def main():

                        # Lernprogramm
#-----------------------------------------------------------------------------#
    try:
        # Begruessung   
        print("\nWilkommen zum Lernprogramm")
        print("Bitte beachten Sie die Gross,- und Kleinschreibung")
        print("Bitte waehlen Sie ihre Csv-Datei aus")

        # Instanz ohne jeglichen Attribute, 
        # um auf Klassenmethoden zuzugreifen
        karteikarte = kk.Karteikarten(None,None,None)

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



        # Karteiprogramm fuer Box 1
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




    #                         # Statistik
    # #-------------------------------------------------------------------------#
        # Gebe Statistik ueber gestelle Fragen aus
        karteikarte.getStatisticOfQuestion()
        # Gebe aus, wie viele Fragen noch in den Boxen
        karteikarte.getNumberOfQuestions(box1)
        # schaue, ob alle Fragen beantwortet wurden
        final_answer = karteikarte.getFinalAnswer(box1)
    # #-------------------------------------------------------------------------#



    #                       #### Finales Ergebnis
    # #----------------------------------------------------------------------------#
        # Wenn alle richtig Fragen beantwortet worden sind, 
        # erstelle Datenbank
        if final_answer == True:

                            # Datenbank
        #----------------------------------------------------------------------#    
            db.createDatabase()
            print("\nCreated Database!")
            print("Die Datenbank ist im Ordner 'database_file' zu finden")
        #----------------------------------------------------------------------#


                            # Matplotlib
        #----------------------------------------------------------------------#
            print("\nMoechten Sie sich das Ergebnis plotten lassen?")
            print("j/n?")

            ask_user_for_plot = ui.ask_for_plot()

            if ask_user_for_plot == "j":
                plot.plot_data()
                sys.exit(0)
            else:
                sys.exit(0)
        #----------------------------------------------------------------------#

    #----------------------------------------------------------------------------#


    # Catche den KeyboardInterrupt hier, 
    # da sont kein Zugriff auf box1 erreicht werden kann
    except KeyboardInterrupt:
        karteikarte.catch_KeyboardInterrupt(box1)
        print("\nProgramm wurde durch KeyBoardInterrupt beendet.")
        print("\nAlle Karten, die noch nicht komplett beantwortet wurden,\nsind wieder in "+ str(box1.name))



                       # Main
#----------------------------------------------------------------------------#
if __name__ == "__main__":
    try:
        main()
    except:
        sys.exit()
#----------------------------------------------------------------------------#