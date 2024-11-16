from classes.led import LedCell
from functions.mix_colors import mixColors

def run(led: LedCell, targetR: int, targetG: int, targetB: int, duration: int, framesExecuted: int):
    redFade = targetR / duration
    greenFade = targetG / duration
    blueFade = targetB / duration

    # print("targetR: %d" % targetR)
    # print("duration: %d" % duration)
    # print("framesExecuted: %d" % framesExecuted)

    fadeTime = duration / 2

    if framesExecuted < fadeTime:
        led.r = min(led.r + redFade, targetR)
        led.g = min(led.g + greenFade, targetG)
        led.b = min(led.b + blueFade, targetB)
    else:
        led.r = max(led.r - redFade, 0)
        led.g = max(led.g - greenFade, 0)
        led.b = max(led.b - blueFade, 0)