from classes.led import LedCell
from classes.scene import Scene
from typing import List
from functions import flash
from math import floor

class SingleLineCascade(Scene):

    # side
    # 0: left
    # 1: top
    # 2: right
    # 3: bottom
    def __init__(self, leds: List[List[LedCell]], startingFrame: int, frameDuration: int, r: int, g: int, b: int, side: int, lineIndex: int):
        self.leds = leds
        self.startingFrame = startingFrame
        self.frameDuration = frameDuration
        self.r = r
        self.g = g
        self.b = b
        self.side = side
        self.lineIndex = lineIndex

        self.cellDuration = frameDuration / 2
        self.cascadeCells = []

        self.stopped = False

        self.setup()

    def setup(self):
       
        if self.side == 0 or self.side == 2:
            for i in range(5):
                cell = self.leds[self.lineIndex][i]
                if (self.side == 0):
                    cell.delay = i * (self.cellDuration / 5)
                else:
                    cell.delay = (4 - i) * (self.cellDuration / 5)
        
        if self.side == 1 or self.side == 3:
            for i in range(6):
                cell = self.leds[i][self.lineIndex]
                if (self.side == 1):
                    cell.delay = i * (self.cellDuration / 5)
                else:
                    cell.delay = (4 - i) * (self.cellDuration / 5)

    

    def run(self, frame: int):

        self.preRun()
        
        if (self.stopped):
            return
        
        if (self.side == 0 or self.side == 2):
            for i in range(5):
                cell = self.leds[self.lineIndex][i]
                if (cell.delay >= frame):
                    continue
                flash.run(cell, self.r, self.g, self.b, self.cellDuration, frame - cell.delay)
        else:
            for i in range(6):
                cell = self.leds[i][self.lineIndex]
                if (cell.delay >= frame):
                    continue

                flash.run(cell, self.r, self.g, self.b, self.cellDuration, frame - cell.delay)

        
