#Dieses Skript dient zum Weiterverarbeitung der Daten
#J. Kempf 2020-04-22

#########################################################################################################
#Bibliotheken importieren (import library)
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
Abbruch = True:

#Zuweisung der Erstellfunktion zu einer Variable (Assignment of the creation variable to a variable)
my_reader = SimpleMFRC522

#Leseanweisung und Ausgabe der eingelesenen Daten (Reading instructions and output of the read data)
while Abbruch:
    try:
        id, my_text = my_reader.read()
        Abbruch = False

    finally:
        GPIO.cleanup()
#########################################################################################################

import time

if (id == 733256096369 ):
    #Festlegung des Pins für die Steuerung
    servoPIN = 22
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50) # GPIO 22 als PWM mit 50Hz
    p.start(2.5) # Initialisierung
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)

    #Prozess stoppen und alle GPIO auf Input stellen
    p.stop()  
    GPIO.cleanup()

else:
    print("Der Benutzer ist nicht autorisiert")
    Abbruch = True
