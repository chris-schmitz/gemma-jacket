from touchio import TouchIn
import adafruit_dotstar as dotstar
import time
import board
import neopixel


jewel = neopixel.NeoPixel(board.A1, 7, brightness=0.1, auto_write=True)
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

touchL = TouchIn(board.A0)
touchR = TouchIn(board.A2)
touchL.threshold = touchL.raw_value + 200
touchR.threshold = touchR.raw_value + 200


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

        elif pattern == 'extend':
            print("==============================")
            print("direction: %s" % self.direction)

            if self.direction == 'forward':
                self.count += 1
                if self.count >= 6:
                    self.direction = 'reverse'
            else:
                self.count -= 1
                if self.count < 0:
                    self.direction = 'forward'

            print("count: %s" % self.count)
            print("==============================")
            if self.direction == 'forward':
                self.jewel[self.count] = self.colorPositions[2]
            else:
                self.jewel[self.count] = self.colorPositions[0]

        time.sleep(.1)


hoodie = Hoodie(jewel)

while True:
    # print(touchL.raw_value)
    if touchL.value and touchR.value:
        print("touched both")
        jewel.fill((255, 255, 255))

    elif touchL.value:
        print("touched left")
        dot[0] = [0, 255, 0]
        hoodie.handleColor('wheel')

    elif touchR.value:
        print("touched right")
        dot[0] = [0, 255, 0]
        hoodie.handleColor('extend')

    else:
        dot[0] = [255, 0, 0]
        jewel.fill((255, 0, 0))
