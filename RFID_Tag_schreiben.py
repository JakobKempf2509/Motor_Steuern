#!/usr/bin/env python

###################################################################################################
#Dieser Programmcode dient zum schreiben von RFID-Tags (This programm code is used to write RFID-Tags)
#J. Kempf 2020-04-22
###################################################################################################

#Bibliotheken importieren (import library)
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

#Zuweisung der Erstellfunktion zu einer Variable (Assignment of the creation variable to a variable)
my_reader = SimpleMFRC522()

#Schreibanweisung und Ausgabe der eingelesenen Daten (Writing instructions and output of the read data)
try:
        my_text_write = input('What do you want to safe on the RFID-Tag? Please write your informations down:\n')
        print("Please place your tag on the RDIF-Reader to write.")
        my_reader.write(my_text_write)
        print("Your information was written correctly.")

finally:
        GPIO.cleanup()