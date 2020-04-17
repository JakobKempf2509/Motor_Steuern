#mit diesem Programmcode wird ein DC Motor mittels Raspberry Pi angesteuert
#J. Kempf 2020-04-17

import RPI.GPIO as GPIO #Zugriff auf das GPIO-Modul
from time import sleep #Aktivierung der Modulzeit

GPIO.setmode(GPIO.BOARD)

#Zuordnung der Pins, damit später auch die Drehrichtung festgelegt werden kann
my_Motor_1_A = 16
my_Motor_1_B = 18
my_Motor_1_C = 22

#Zuweisung, dass alle Pins Ausgänge sind
GPIO.setup(my_Motor_1_A , GPIO.OUT)
GPIO.setup(my_Motor_1_B , GPIO.OUT)
GPIO.setup(my_Motor_1_C , GPIO.OUT)

#Anlegen der Nachrichten
message_1 = "Der Motor wird eingeschalten"
message_2 = "Der Motor wird ausgeschalten"

#Einschalten
#Mit Motor_1_A und Motor_1_B kann die Drehrichtung festgelegt werden (abhängig von low und high)
print(message_1)
GPIO.output(my_Motor_1_A , GPIO.HIGH)
GPIO.output(my_Motor_1_B , GPIO.LOW)
GPIO.output(my_Motor_1_C , GPIO.HIGH)

#Wartezeit
sleep(5)

#Ausschalten
print(message_2)
GPIO.output(my_Motor_1_C , GPIO.LOW)

GPIO.cleanup()