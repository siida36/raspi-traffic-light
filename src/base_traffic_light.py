import time
import RPi.GPIO as GPIO


class BaseTrafficLight():

    @property
    def gpio_blue(self) -> int:
        return self._gpio_blue

    @gpio_blue.setter
    def gpio_blue(self, val: int):
        self._gpio_blue = val

    @property
    def gpio_yellow(self) -> int:
        return self._gpio_yellow

    @gpio_yellow.setter
    def gpio_yellow(self, val: int):
        self._gpio_yellow = val

    @property
    def gpio_red(self) -> int:
        return self._gpio_red

    @gpio_red.setter
    def gpio_red(self, val: int):
        self._gpio_red = val


    def __init__(self):
        self.gpio_blue = 16
        self.gpio_yellow = 20
        self.gpio_red = 21

        self.all_gpio_pins = [
            self.gpio_blue, self.gpio_yellow, self.gpio_red,
        ]

        for gpio_pin in self.all_gpio_pins:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(gpio_pin, GPIO.OUT)

    def __call__(self):
        """メインルーチン"""
        while True:
            self.lit_light(self.gpio_blue, 3)
            self.lit_light(self.gpio_yellow, 3)
            self.lit_light(self.gpio_red, 3)

    def lit_light(self, gpio_pin: int, lit_time: int):
        GPIO.output(gpio_pin, 1)

        time.sleep(lit_time)
        GPIO.output(gpio_pin, 0)

    def __del__(self):
        for gpio_pin in self.all_gpio_pins:
            GPIO.output(gpio_pin, 0)


if __name__ == "__main__":
    traffic_light = BaseTrafficLight()
    traffic_light()
