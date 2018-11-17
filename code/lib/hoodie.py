import time


class Hoodie:
    def __init__(self, jewel):
        self.jewel = jewel

    # * Public constants to denote useable patterns
    WHEEL = 0
    EXTEND = 1
    HOP = 2

    # * Define private properties
    _count = 0
    _direction = 'forward'

    # * Define private constants
    _RED = (255, 0, 0)
    _MAGENTA = (255, 0, 255)
    _PURPLE = (149, 66, 244)
    _CYAN = (0, 255, 255)
    _DARKGREEN = (15, 79, 80)
    _GOLD = (255, 216, 0)
    _BLUEISH = (46, 0, 255)

    _COLORPOSITIONS = [_RED, _MAGENTA, _PURPLE,
                       _CYAN, _DARKGREEN, _GOLD, _BLUEISH]

    def handleColor(self, pattern):
        if pattern == self.WHEEL:
            self._wheelPattern()
        elif pattern == self.EXTEND:
            self._extendPattern()
        elif pattern == self.HOP:
            self._hopPattern()
        time.sleep(.1)

    def _wheelPattern(self):
        self._count += 1
        if self._count > 6:
            self._count = 0

        self.jewel[0] = self._COLORPOSITIONS[2]
        self.jewel[1] = self._COLORPOSITIONS[5-self._count]
        self.jewel[2] = self._COLORPOSITIONS[4-self._count]
        self.jewel[3] = self._COLORPOSITIONS[3-self._count]
        self.jewel[4] = self._COLORPOSITIONS[2-self._count]
        self.jewel[5] = self._COLORPOSITIONS[1-self._count]
        self.jewel[6] = self._COLORPOSITIONS[self._count]

    def _extendPattern(self):
        if self._direction == 'forward':
            self._count += 1

            if self._count >= 6:
                self._direction = 'reverse'
        else:
            self._count -= 1

            if self._count < 0:
                self._direction = 'forward'

        if self._direction == 'forward':
            self.jewel[self._count] = self._COLORPOSITIONS[2]
        else:
            self.jewel[self._count] = self._COLORPOSITIONS[0]

    def _hopPattern(self):
        self.jewel.fill(self._RED)

        pause = 0.5

        self.jewel[1] = self._DARKGREEN
        time.sleep(pause)
        self.jewel[4] = self._DARKGREEN
        time.sleep(pause)

        self.jewel[2] = self._DARKGREEN
        time.sleep(pause)
        self.jewel[5] = self._DARKGREEN
        time.sleep(pause)

        self.jewel[3] = self._DARKGREEN
        time.sleep(pause)
        self.jewel[6] = self._DARKGREEN

        time.sleep(pause)
        self.jewel[0] = self._DARKGREEN
        time.sleep(pause)

        self.jewel.fill(self._RED)
        time.sleep(pause)
