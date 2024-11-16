from classes.led import LedCell
from classes.scene import Scene
from typing import List
from functions import flash
from math import floor

class SideCascade(Scene):

    # side
    # 0: left
    # 1: top
    # 2: right
    # 3: bottom
    def __init__(self, leds: List[List[LedCell]], startingFrame: int, frameDuration: int, r: int, g: int, b: int, side: int):
        self.leds = leds
        self.startingFrame = startingFrame
        self.frameDuration = frameDuration
        self.r = r
        self.g = g
        self.b = b
        self.side = side

        self.cellDuration = frameDuration / 2
        self.cellDelays = []

        self.setup()

    def setup(self):
       for i in range(len(self.leds)):

            rowDelays = []

            for j in range(len(self.leds[i])):
                
                cell = self.leds[i][j]
                cell.r = 0
                cell.g = 0
                cell.b = 0

                match self.side:
                    # left
                    case 0:
                        delay = i * (self.cellDuration / 6)
                    # top
                    case 1:
                        delay = j * (self.cellDuration / 5)
                    # right
                    case 2:
                        delay = (5 - i) * (self.cellDuration / 6)
                    # bottom
                    case 3:
                        delay = (5 - j) * (self.cellDuration / 5)

                rowDelays.append(delay)

            self.cellDelays.append(rowDelays)
    

    def run(self, frame: int):
        for row in self.leds:
            for cell in row:
                delay = self.cellDelays[cell.xI][cell.yI]

                if delay >= frame: # or (cell.delay + frame > cell.delay + self.cellDuration):
                    continue
                flash.run(cell, self.r, self.g, self.b, self.cellDuration, frame - delay)