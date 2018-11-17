import time


class Hoodie:
    def __init__(self, jewel):
        self.jewel = jewel

    count = 0
    direction = 'forward'

    red = (255, 0, 0)
    magenta = (255, 0, 255)
    purple = (149, 66, 244)
    cyan = (0, 255, 255)
    darkGreen = (15, 79, 80)
    gold = (255, 216, 0)
    blueish = (46, 0, 255)

    colorPositions = [red, magenta, purple, cyan, darkGreen, gold, blueish]

    def handleColor(self, pattern):
        if pattern == 'wheel':
            self._wheelPattern()
        elif pattern == 'extend':
            self._extendPattern()
        elif pattern == 'hop':
            self._hopPattern()
        time.sleep(.1)

    def _wheelPattern(self):
        self.count += 1
        if self.count > 6:
            self.count = 0

        self.jewel[0] = self.colorPositions[2]
        self.jewel[1] = self.colorPositions[5-self.count]
        self.jewel[2] = self.colorPositions[4-self.count]
        self.jewel[3] = self.colorPositions[3-self.count]
        self.jewel[4] = self.colorPositions[2-self.count]
        self.jewel[5] = self.colorPositions[1-self.count]
        self.jewel[6] = self.colorPositions[self.count]

    def _extendPattern(self):
        if self.direction == 'forward':
            self.count += 1

            if self.count >= 6:
                self.direction = 'reverse'
        else:
            self.count -= 1

            if self.count < 0:
                self.direction = 'forward'

        if self.direction == 'forward':
            self.jewel[self.count] = self.colorPositions[2]
        else:
            self.jewel[self.count] = self.colorPositions[0]

    def _hopPattern(self):
        self.jewel.fill(self.colorPositions[0])

        pause = 0.5
        self.jewel[1] = self.colorPositions[4]
        time.sleep(pause)
        self.jewel[4] = self.colorPositions[4]
        time.sleep(pause)

        self.jewel[2] = self.colorPositions[4]
        time.sleep(pause)
        self.jewel[5] = self.colorPositions[4]
        time.sleep(pause)

        self.jewel[3] = self.colorPositions[4]
        time.sleep(pause)
        self.jewel[6] = self.colorPositions[4]

        time.sleep(pause)
        self.jewel[0] = self.colorPositions[4]
        time.sleep(pause)

        self.jewel.fill(self.colorPositions[0])
        time.sleep(pause)
