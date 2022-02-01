
   _____ ____  __    ________ _       ______  ____  __ _______
  / ___// __ \/ /   /  _/ __ \ |     / / __ \/ __ \/ //_/ ___/
  \__ \/ / / / /    / // / / / | /| / / / / / /_/ / ,<  \__ \ 
 ___/ / /_/ / /____/ // /_/ /| |/ |/ / /_/ / _, _/ /| |___/ / 
/____/\____/_____/___/_____/ |__/|__/\____/_/ |_/_/ |_/____/  
                                                              
***Konstruktion in SOLIDWORKS***
Um die Position der Kamera zu ändern, können die Parameter X,Y,Z und BlickX, BlickY verändert werden.
Das Koordinatensystem ist gleich ausgerichtet, wie das von SOLIDWORKS


***Externe Referenzen***
In der Baugruppe sind die externen Referenzen gesperrt.
Die externen Referenzen sind anahand des Pfeil Symbols im Featurebaum erkennbar
-> = Externe Referenz
->* = gesperrte externe Referenz
Damit sich der Adapter und die Kamerahalterung an eine geänderte Position anpassen, müssen die Referezen entsperrt werden.
(Rechtsklick auf Feature > "Externe Referenzen"

    ____        __  __              
   / __ \__  __/ /_/ /_  ____  ____ 
  / /_/ / / / / __/ __ \/ __ \/ __ \
 / ____/ /_/ / /_/ / / / /_/ / / / /
/_/    \__, /\__/_/ /_/\____/_/ /_/ 
      /____/                        
***Installation von EXIFtool***

Download und Anleitung unter https://exiftool.org/install.html


***Installation der Libraries***

FlirImageExtractor:
https://pypi.org/project/flirimageextractor/

NumPy:
https://numpy.org/install/

matplotlib:
https://matplotlib.org/stable/users/installing.html


***Anpassung der FlirImageExtrator Library***
Bei ersten Durchlauf hat bei mir die Library "EXIFtool" nicht gefunden...
Um dies zu Lösen kann in der FlirImageExtractor Library der Dateipfad von EXIFtool händisch eingegeben werden
--> Bei Zeile 21:  exiftool_path="C:/Users/##/exiftool.exe" den Dateipfad ersetzen

Bei Wärmebildern, die über die Live-Übertragungsfunktion in "FLIR Tools" gemacht wurden fehlen GPS Informationen.
Dabei wird von EXIFTool ein Fehler ausgegeben der durch hinzufügen eines Attributs unterdrückt werden kann.
--> Zeile 233 ersetzen mit: [self.exiftool_path, "-RawThermalImage", "-b", "-q", "-q", self.flir_img_filename]

***Python Programm***

Erklärung der Variablen:
splits = <Wie oft das Wärmebild unterteilt werden soll>

cuttoffy = <Abschneiden des unteren Teils>
addy = <Versetzen des Bildes um die y-Achse>
addx = <Versetzten um x-Achse>

working_dir = <Pfad des Wärmebildes> !! Ohne Suffix angeben !!

image_number = <Anfangsnummer der Wärmebilder>
anzahl_bilder = <Anzahl der Bilder die gestapelt werden sollen>
-> Bsp.: 10 Wärmebilder liegen am Desktop mit Namen "Testbild 1.jpg" bis "Testbild 11.jpg"
	--> working_dir = "C:/Users/johan/Desktop/Testbild "
	--> image_number = 1
	--> anzahl_bilder = 10
-> Somit werden die 10 Wärmebilder ausgewertet

temp_min und temp_max = Temperaturbereich in dem die Bilder untersucht werden. Kann mit der change_mask(lower,upper) funktion gezielt festgelegt werden

Erklärung der Funktionen:
get_... Funktionen = erfassung von statistischen Kenngrößen

print/show - Funktionen = Ausgabe von statistischen Kenngrößen in der Konsole/ Anzeigen einer Zone

auswertung() Funktion = Ausgabe der statistischen Daten aller Zonen in die Konsole


Bei weiteren Fragen bin ich erreichbar unter: jojo.picker@gmail.com

