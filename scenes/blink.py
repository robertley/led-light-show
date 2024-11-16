import time
import neopixel
from classes.led import LedCell

from typing import List

def run(neo: neopixel, leds: List[List[LedCell]], beatLength: int, r: int, g: int, b: int):
    flashLength = beatLength / 2
    for row in leds:
        for cell in row:
            neo[cell.sI] = (r, g, b)

    neo.show()
    time.sleep(flashLength)

    for row in leds:
        for cell in row:
            neo[cell.sI] = (0, 0, 0)

    neo.show()
    time.sleep(flashLength)