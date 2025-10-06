import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)





print("High")
GPIO.output(17, GPIO.HIGH)
time.sleep(3)
print("Low")
GPIO.output(17, GPIO.LOW)
