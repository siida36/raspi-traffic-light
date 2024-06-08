import time
import RPi.GPIO as GPIO

GPIO_BLUE = 16
GPIO_YELLOW = 20
GPIO_RED = 21

for GPIO_PIN in [GPIO_BLUE, GPIO_YELLOW, GPIO_RED]:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.OUT)
    GPIO.output(GPIO_PIN, 1)

    time.sleep(3)
    GPIO.output(GPIO_PIN, 0)
