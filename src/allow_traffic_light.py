import time
import RPi.GPIO as GPIO

from base_traffic_light import BaseTrafficLight


class AllowTrafficLight(BaseTrafficLight):

    @property
    def gpio_left_allow(self) -> int:
        return self._gpio_left_allow

    @gpio_left_allow.setter
    def gpio_left_allow(self, val: int):
        self._gpio_left_allow = val

    @property
    def gpio_center_allow(self) -> int:
        return self._gpio_center_allow

    @gpio_center_allow.setter
    def gpio_center_allow(self, val: int):
        self._gpio_center_allow = val

    @property
    def gpio_right_allow(self) -> int:
        return self._gpio_right_allow

    @gpio_right_allow.setter
    def gpio_right_allow(self, val: int):
        self._gpio_right_allow = val

    def __init__(self):
        self.gpio_blue = 16
        self.gpio_yellow = 20
        self.gpio_red = 21
        self.gpio_left_allow = 17
        self.gpio_center_allow = 27
        self.gpio_right_allow = 22

        self.all_gpio_pins = [
            self.gpio_blue, self.gpio_yellow, self.gpio_red,
            self.gpio_left_allow, self.gpio_center_allow, self.gpio_right_allow,
        ]

        for gpio_pin in self.all_gpio_pins:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(gpio_pin, GPIO.OUT)

    def __call__(self):
        """メインルーチン"""
        while True:
            self.lit_multi_lights([self.gpio_red, self.gpio_left_allow, self.gpio_center_allow], 3)
            self.lit_light(self.gpio_blue, 3)
            self.lit_light(self.gpio_yellow, 3)
            self.lit_multi_lights([self.gpio_red, self.gpio_right_allow], 3)
            self.lit_light(self.gpio_red, 3)

    def lit_multi_lights(self, gpio_pins: list[int], lit_time: int):
        for gpio_pin in gpio_pins:
            GPIO.output(gpio_pin, 1)

        time.sleep(lit_time)
        for gpio_pin in gpio_pins:
            GPIO.output(gpio_pin, 0)


if __name__ == "__main__":
    traffic_light = AllowTrafficLight()
    traffic_light()
