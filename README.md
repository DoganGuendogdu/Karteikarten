# 1 Einfuehrung 

## 1.1 Ziel und Intention
Das Lernprogramm verfolgt das klassische Prinzip des Karteilernens.

Intention der Entwicklung ist das Selbstudium mit Python.
Das Programm ist mit Absicht auf Deutsch entwickelt worden,  
da es auch im privaten Gebrauch meinerseits zu Gebrauch kommt. 
Weitere Projekte sind definitiv auf Englisch geplant.

## 1.2 Einfuehrung in das Prinzip des Lernprogramms:
### Deutsch   
https://de.wikipedia.org/wiki/Lernkartei

### Englisch 
https://en.wikipedia.org/wiki/Flashcard


# 2 installation
```
git clone https://github.com/DoganGuendogdu/Karteikarten.git 
cd Karteikarten
pip3 install -r requirement.txt
python3 main.py
```
# 3 Dokumentation

## 3.1 Kriterien der einzulesenen Datei
 1. Es sind lediglich Dateien im CSV-Format erlaubt.
 2. Frage und Anwort muessen durch ein **Komma** getrennt werden  
 3. Hierbei spielen White Spaces **keine** Rolle
 
 ### 3.1.1 Beispiel CSV
 <img src = "images/questions_answers.png" width = "650">


## 3.2 Ablauf Programm 

### 3.2.1 Datei entgegennehmen
<img src = "images/input.jpg"> 
  
### 3.2.2 Lernprogramm
<img src ="images/program.png">

### 3.2.3 Ergebnis der Lernsession
Nach Ende des Durchlaufs wird eine Statistik mit Anzahl der Fragen  
sowie der prozentuale Wert des Lernerfolgs festgelegt.  
<img src = "images/statistics.png"> 

### 3.2.4 weitere Lernsessions
Wenn nach dem ersten Durchlauf noch Karten in der ersten Box,  
also der eingelesenen Datei existieren,  
so muss fuer die naechsten Durchlaeufe dieselbe Datei zu Beginn eingelesen werden.

Nach der ersten Session ist zu sehen,  
wie oft die gestellte Frage falsch oder richtig beantwortet worden ist.    
<img src = "images/after_session.png"> 

### 3.2.5 Datenbank
Wenn **alle** Fragen in der eingelesenen Datei erfolgreich beantwortet worden sind,  
so wird automatisch eine Datenbank mittels sqlite3 erstellt.
<img src = "images/database.png"> 

### 3.2.6 Plot Ergebnis
Bei Bedarf kann der User entscheiden, ob das Ergebnis geplotet werden soll.  
<img src = "images/plot.png"> 






