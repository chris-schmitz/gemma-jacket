from touchio import TouchIn
import adafruit_dotstar as dotstar
import board
import neopixel
from hoodie import Hoodie
import time


jewel = neopixel.NeoPixel(board.A1, 7, brightness=0.1, auto_write=True)
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

touchL = TouchIn(board.A0)
touchR = TouchIn(board.A2)
touchL.threshold = touchL.raw_value + 200
touchR.threshold = touchR.raw_value + 200


hoodie = Hoodie(jewel)

ORDER = neopixel.GRB
num_pixels = 7


while True:
    # print(touchL.raw_value)

    if touchL.value and touchR.value:
        print("touched both")
        hoodie.handleColor('hop')
        # jewel.fill((255, 255, 255))

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
