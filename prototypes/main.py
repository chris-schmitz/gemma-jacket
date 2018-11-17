from touchio import TouchIn
import adafruit_dotstar as dotstar
import time
import board
import neopixel


jewel = neopixel.NeoPixel(board.A1, 7, brightness=0.1, auto_write=True)
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

touch = TouchIn(board.A0)
# touch.threshold = touch.raw_value - 50
touch.threshold = touch.raw_value + 100

count = 0


def handleColor(count, jewel):
    red = (255, 0, 0)
    magenta = (255, 0, 255)
    purple = (149, 66, 244)
    color4 = (0, 255, 255)
    color5 = (0, 0, 255)
    color6 = (0, 255, 0)
    color7 = (0, 255, 50)

    colorPositions = [red, magenta, purple, color4, color5, color6, color7]
    count += 1

    if count > 6:
        count = 0

    jewel[0] = colorPositions[2]
    jewel[1] = colorPositions[5-count]
    jewel[2] = colorPositions[4-count]
    jewel[3] = colorPositions[3-count]
    jewel[4] = colorPositions[2-count]
    jewel[5] = colorPositions[1-count]
    jewel[6] = colorPositions[count]

    time.sleep(.1)
    return count


while True:
    print(touch.raw_value)
    if not touch.value:
        print("touched")
        dot[0] = [0, 255, 0]
        count = handleColor(count, jewel)
    else:
        dot[0] = [255, 0, 0]
        jewel.fill((255, 0, 0))
