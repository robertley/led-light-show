from classes.led import LedCell
from functions.mix_colors import mixColors

def run(led: LedCell, targetR: int, targetG: int, targetB: int, duration: int):
    redFade = targetR / duration
    greenFade = targetG / duration
    blueFade = targetB / duration

    led.r = min(led.r + redFade, targetR)
    led.g = min(led.g + greenFade, targetG)
    led.b = min(led.b + blueFade, targetB)