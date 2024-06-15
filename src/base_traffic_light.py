import time
import RPi.GPIO as GPIO

from raspi_led_light import RasPiLEDLight


class BaseTrafficLight():

    @property
    def blue_light(self) -> RasPiLEDLight:
        return self._blue_light

    @blue_light.setter
    def blue_light(self, val: RasPiLEDLight):
        self._blue_light = val

    @property
    def yellow_light(self) -> RasPiLEDLight:
        return self._yellow_light

    @yellow_light.setter
    def yellow_light(self, val: RasPiLEDLight):
        self._yellow_light = val

    @property
    def red_light(self) -> RasPiLEDLight:
        return self._red_light

    @red_light.setter
    def red_light(self, val: RasPiLEDLight):
        self._red_light = val

    def __init__(self):
        self.blue_light = RasPiLEDLight(color="blue", gpio=16)
        self.yellow_light = RasPiLEDLight(color="yellow", gpio=20)
        self.red_light = RasPiLEDLight(color="red", gpio=21)

        self.all_lights = [
            self.blue_light, self.yellow_light, self.red_light,
        ]

        for light in self.all_lights:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(light.gpio, GPIO.OUT)

    def __call__(self):
        """メインルーチン"""
        while True:
            self.lit_light(self.blue_light, 3)
            self.lit_light(self.yellow_light, 3)
            self.lit_light(self.red_light, 3)

    def lit_light(self, light: RasPiLEDLight, lit_time: int):
        GPIO.output(light.gpio, 1)

        time.sleep(lit_time)
        GPIO.output(light.gpio, 0)

    def __del__(self):
        for light in self.all_lights:
            GPIO.output(light.gpio, 0)


if __name__ == "__main__":
    traffic_light = BaseTrafficLight()
    traffic_light()
