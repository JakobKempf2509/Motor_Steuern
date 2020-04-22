import RPi.GPIO as GPIO
import time

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