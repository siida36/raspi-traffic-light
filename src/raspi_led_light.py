class RasPiLEDLight():
    """ラズパイを電力源としたLEDライトを表現します。"""

    @property
    def color(self) -> str:
        """色を定義します。

        次のいずれかの文字列のみ許容します。
        - red
        - yellow
        - blue
        """
        return self._color

    @color.setter
    def color(self, val: str):
        self._color = val

    @property
    def gpio(self) -> int:
        """電力源となるラズパイのGPIOピンの番号を指定します。"""
        return self._gpio

    @gpio.setter
    def gpio(self, val: int):
        self._gpio = val

    def __init__(self, color: str, gpio: int):
        """色とGPIO番号を指定するためのコンストラクタです。"""
        self.color = color
        self.gpio = gpio
