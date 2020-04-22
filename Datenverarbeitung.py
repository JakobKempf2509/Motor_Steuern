#!/usr/bin/env python

#Dieses Skript dient zum Weiterverarbeitung der Daten
#J. Kempf 2020-04-22

#########################################################################################################
#Bibliotheken importieren (import library)
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

#benötigte Festlegungen
abbruch = True
Benutzer_1 = 733256096369

#Zuweisung der Erstellfunktion zu einer Variable (Assignment of the creation variable to a variable)
my_reader = SimpleMFRC522()

#Schleife zur Steuerung des Motors mit Freigabe (loop to control the engine with release)
while abbruch:
    try:
        #Zuweisung der ID und des Inhalts des Tags
        print("Bitte autorisieren Sie sich als Benutzer indem Sie ihren RFID-Tag auf den Leser legen")
        id, my_text = my_reader.read()
        GPIO.cleanup()

        #If-Bedingung für richtige ID
        if (id == Benutzer_1):
            print("Der Benutzer ist für die gewünschte Anforderung autorisiert")

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
            print("Die gewüschte Anwendung wurde erfolgreich durchgeführt.\nDie Anwendung wird im Anschluss beendet.")
            GPIO.cleanup()
            abbruch = False

        else:
            print("Sie sind als Benutzer nicht für diese Anwendung autorisiert, bitte versuchen Sie es nochmal")

    except ValueError:
        print("Es gab einen Fehler bei dem gewünschten Prozess, bitte versuchen Sie es erneut")