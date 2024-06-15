import time
import RPi.GPIO as GPIO

from base_traffic_light import BaseTrafficLight
from raspi_led_light import RasPiLEDLight


class AllowTrafficLight(BaseTrafficLight):

    @property
    def left_allow_light(self) -> RasPiLEDLight:
        return self._left_allow_light

    @left_allow_light.setter
    def left_allow_light(self, val: RasPiLEDLight):
        self._left_allow_light = val

    @property
    def center_allow_light(self) -> RasPiLEDLight:
        return self._center_allow_light

    @center_allow_light.setter
    def center_allow_light(self, val: RasPiLEDLight):
        self._center_allow_light = val

    @property
    def right_allow_light(self) -> RasPiLEDLight:
        return self._right_allow_light

    @right_allow_light.setter
    def right_allow_light(self, val: RasPiLEDLight):
        self._right_allow_light = val

    def __init__(self):
        self.blue_light = RasPiLEDLight(color="blue", gpio=16)
        self.yellow_light = RasPiLEDLight(color="yellow", gpio=20)
        self.red_light = RasPiLEDLight(color="red", gpio=21)

        self.left_allow_light = RasPiLEDLight(color="blue", gpio=17)
        self.center_allow_light = RasPiLEDLight(color="blue", gpio=27)
        self.right_allow_light = RasPiLEDLight(color="blue", gpio=22)

        self.all_lights = [
            self.blue_light, self.yellow_light, self.red_light,
            self.left_allow_light, self.center_allow_light, self.right_allow_light,
        ]

        for light in self.all_lights:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(light.gpio, GPIO.OUT)

    def __call__(self):
        """メインルーチン"""
        while True:
            self.lit_multi_lights([self.red_light, self.left_allow_light, self.center_allow_light], 3)
            self.lit_light(self.blue_light, 3)
            self.lit_light(self.yellow_light, 3)
            self.lit_multi_lights([self.red_light, self.right_allow_light], 3)
            self.lit_light(self.red_light, 3)

    def lit_multi_lights(self, lights: list[RasPiLEDLight], lit_time: int):
        for light in lights:
            GPIO.output(light.gpio, 1)

        time.sleep(lit_time)
        for light in lights:
            GPIO.output(light.gpio, 0)


if __name__ == "__main__":
    traffic_light = AllowTrafficLight()
    traffic_light()
