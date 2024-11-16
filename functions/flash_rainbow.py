from classes.led import LedCell
from functions.mix_colors import mixColors

def run(led: LedCell, duration: int, framesExecuted: int):
    fade = 255 / duration * 4
    redFadeTime = duration / 4
    blueFadeTime = duration / 4 + redFadeTime
    greenFadeTime = duration / 4 + blueFadeTime

    if framesExecuted < redFadeTime:
        led.r = min(led.r + fade, 255)
    else:
        led.r = max(led.r - fade, 0)
    
    if framesExecuted < blueFadeTime and framesExecuted > redFadeTime:
        led.b = min(led.b + fade, 255)
    else:
        led.b = max(led.b - fade, 0)
    
    if framesExecuted < greenFadeTime and framesExecuted > blueFadeTime:
        led.g = min(led.g + fade, 255)
    else:
        led.g = max(led.g - fade, 0)

    # redFade = targetR / duration
    # greenFade = targetG / duration
    # blueFade = targetB / duration

    # # print("targetR: %d" % targetR)
    # # print("duration: %d" % duration)
    # # print("framesExecuted: %d" % framesExecuted)

    # fadeTime = duration / 2

    # if framesExecuted < fadeTime:
    #     led.r = min(led.r + redFade, targetR)
    #     led.g = min(led.g + greenFade, targetG)
    #     led.b = min(led.b + blueFade, targetB)
    # else:
    #     led.r = max(led.r - redFade, 0)
    #     led.g = max(led.g - greenFade, 0)
    #     led.b = max(led.b - blueFade, 0)
    