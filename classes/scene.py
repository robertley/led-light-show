from typing import List, Callable
from classes.led import LedCell

class Scene:

    firstRun = True
    stopped = False
    startCallback: Callable = None

    def __init__(self, leds: List[List[LedCell]], startingFrame: int, frameDuration: int, r: int, g: int, b: int):
        self.leds = leds
        self.startingFrame = startingFrame
        self.frameDuration = frameDuration
        self.r = r
        self.g = g
        self.b = b

    def clearCells(self):
        for row in self.leds:
            for cell in row:
                cell.reset()

    def stop(self):
        self.clearCells()
        self.stopped = True

    def preRun(self):
        if (self.firstRun):
            if (self.startCallback):
                self.startCallback()
            self.firstRun = False