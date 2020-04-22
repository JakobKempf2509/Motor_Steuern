#!/usr/bin/env python

###################################################################################################
#Dieser Programmcode dient zum lesen von RFID-Tags (This programm code is used to read RFID-Tags)
#J. Kempf 2020-04-22
###################################################################################################

#Bibliotheken importieren (import library)
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

#Zuweisung der Erstellfunktion zu einer Variable (Assignment of the creation variable to a variable)
my_reader = SimpleMFRC522

#Leseanweisung und Ausgabe der eingelesenen Daten (Reading instructions and output of the read data)
try:
    id, my_text = my_reader.read()

finally:
    GPIO.cleanup()