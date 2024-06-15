import time
import RPi.GPIO as GPIO

from raspi_led_light import RasPiLEDLight


class BaseTrafficLight():
    """青・黄・赤の信号を持つ基本的な信号機を定義します。"""

    @property
    def blue_light(self) -> RasPiLEDLight:
        """青信号を定義します。"""
        return self._blue_light

    @blue_light.setter
    def blue_light(self, val: RasPiLEDLight):
        self._blue_light = val

    @property
    def yellow_light(self) -> RasPiLEDLight:
        """黄信号を定義します。"""
        return self._yellow_light

    @yellow_light.setter
    def yellow_light(self, val: RasPiLEDLight):
        self._yellow_light = val

    @property
    def red_light(self) -> RasPiLEDLight:
        """赤信号を定義します。"""
        return self._red_light

    @red_light.setter
    def red_light(self, val: RasPiLEDLight):
        self._red_light = val

    def __init__(self):
        """最初にセットアップを実施するための関数です。"""
        # NOTE: 属性をセットします。
        self.blue_light = RasPiLEDLight(color="blue", gpio=16)
        self.yellow_light = RasPiLEDLight(color="yellow", gpio=20)
        self.red_light = RasPiLEDLight(color="red", gpio=21)

        self.all_lights = [
            self.blue_light, self.yellow_light, self.red_light,
        ]

        # NOTE: GPIOの初期化を実行します。
        for light in self.all_lights:
            GPIO.setmode(GPIO.BCM)  # NOTE: BCM形式でピンを指定できるようにします。
            GPIO.setup(light.gpio, GPIO.OUT)  # NOTE: 出力ポートとして使用するようにします。

    def __call__(self):
        """メインルーチンを実装したものです。"""

        # NOTE: LEDを順番に点灯させる処理を無限に繰り返します。
        while True:
            self.lit_light(light=self.blue_light, lit_time=3)
            self.lit_light(light=self.yellow_light, lit_time=3)
            self.lit_light(light=self.red_light, lit_time=3)

    def lit_light(self, light: RasPiLEDLight, lit_time: int):
        """LEDを指定した時間だけ点灯します。"""
        GPIO.output(light.gpio, 1)

        time.sleep(lit_time)
        GPIO.output(light.gpio, 0)

    def __del__(self):
        """終了時にLEDをすべて消灯するための処理です。"""
        for light in self.all_lights:
            GPIO.output(light.gpio, 0)


if __name__ == "__main__":
    traffic_light = BaseTrafficLight()  # NOTE: __init__() が実行されます。
    traffic_light()  # NOTE: __call__() が実行されます。
