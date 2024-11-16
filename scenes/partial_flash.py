from classes.led import LedCell
from classes.scene import Scene
from typing import List, Callable
from functions import flash
from math import floor
from functions.change_brightness import changeBrightness

class PartialFlash(Scene):

    def __init__(self, leds: List[List[LedCell]], startingFrame: int, frameDuration: int, r: int, g: int, b: int, startRow: int, startCol: int, endRow: int, endCol: int, startCallback: Callable = None):
        self.leds = leds
        self.startingFrame = startingFrame
        self.frameDuration = frameDuration
        self.r = r
        self.g = g
        self.b = b
        self.startRow = startRow
        self.startCol = startCol
        self.endRow = endRow
        self.endCol = endCol
        self.startCallback = startCallback

        self.setup()

    def setup(self):
       None
    

    def run(self, frame: int):
        for i in range(self.endRow - self.startRow):
            for j in range(self.endCol - self.startCol):
                cell = self.leds[i + self.startRow][j + self.startCol]
                flash.run(cell, self.r, self.g, self.b, self.frameDuration, frame)