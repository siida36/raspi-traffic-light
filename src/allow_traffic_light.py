import time
import RPi.GPIO as GPIO

from base_traffic_light import BaseTrafficLight
from raspi_led_light import RasPiLEDLight


class AllowTrafficLight(BaseTrafficLight):
    """青・黄・赤の信号に加えて、３方向の矢印信号を持つ信号機を定義します。"""

    # NOTE: 子クラスでは矢印信号だけを定義します。
    # 青・黄・赤信号は、親クラスで定義したので省略します。

    @property
    def left_allow_light(self) -> RasPiLEDLight:
        """左矢印信号を定義します。"""
        return self._left_allow_light

    @left_allow_light.setter
    def left_allow_light(self, val: RasPiLEDLight):
        self._left_allow_light = val

    @property
    def center_allow_light(self) -> RasPiLEDLight:
        """中央矢印信号を定義します。"""
        return self._center_allow_light

    @center_allow_light.setter
    def center_allow_light(self, val: RasPiLEDLight):
        self._center_allow_light = val

    @property
    def right_allow_light(self) -> RasPiLEDLight:
        """右矢印信号を定義します。"""
        return self._right_allow_light

    @right_allow_light.setter
    def right_allow_light(self, val: RasPiLEDLight):
        self._right_allow_light = val

    def __init__(self):
        """最初にセットアップを実施するための関数です。"""
        # NOTE: 属性をセットします。

        # NOTE: 矢印信号は子クラスで新たに定義したものです。
        # 上記のようにこのファイルの中で定義しないと使用できません。
        self.left_allow_light = RasPiLEDLight(color="blue", gpio=17)
        self.center_allow_light = RasPiLEDLight(color="blue", gpio=27)
        self.right_allow_light = RasPiLEDLight(color="blue", gpio=22)

        # NOTE: 青・黄・赤信号は親クラスで定義したものを使えます。
        # つまり、このファイルで再び定義する必要はありません。
        self.blue_light = RasPiLEDLight(color="blue", gpio=16)
        self.yellow_light = RasPiLEDLight(color="yellow", gpio=20)
        self.red_light = RasPiLEDLight(color="red", gpio=21)

        self.all_lights = [
            self.blue_light, self.yellow_light, self.red_light,
            self.left_allow_light, self.center_allow_light, self.right_allow_light,
        ]

        # NOTE: GPIOの初期化を実行します。
        for light in self.all_lights:
            GPIO.setmode(GPIO.BCM)  # NOTE: BCM形式でピンを指定できるようにします。
            GPIO.setup(light.gpio, GPIO.OUT)  # NOTE: 出力ポートとして使用するようにします。

    def __call__(self):
        """メインルーチンを実装したものです。"""

        # NOTE: LEDを順番に点灯させる処理を無限に繰り返します。
        # 子クラスではlit_multi_lightsだけを定義しています。
        # lit_lightは親クラスで定義したので省略して使用できます。
        while True:
            self.lit_multi_lights(
                lights=[self.red_light, self.left_allow_light, self.center_allow_light],
                lit_time=3
            )
            self.lit_light(light=self.blue_light, lit_time=3)
            self.lit_light(light=self.yellow_light, lit_time=3)
            self.lit_multi_lights(lights=[self.red_light, self.right_allow_light], lit_time=3)
            self.lit_light(light=self.red_light, lit_time=3)

    def lit_multi_lights(self, lights: list[RasPiLEDLight], lit_time: int):
        """複数のLEDを同時に光らせるための関数です。"""
        for light in lights:
            GPIO.output(light.gpio, 1)

        time.sleep(lit_time)
        for light in lights:
            GPIO.output(light.gpio, 0)


if __name__ == "__main__":
    traffic_light = AllowTrafficLight()  # NOTE: __init__() が実行されます
    traffic_light()  # NOTE: __call__() が実行されます
