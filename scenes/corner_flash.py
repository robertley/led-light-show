from classes.led import LedCell
from classes.scene import Scene
from typing import List
from functions import flash
from math import floor
from functions.change_brightness import changeBrightness

class CornerFlash(Scene):

    def __init__(self, leds: List[List[LedCell]], startingFrame: int, frameDuration: int, r: int, g: int, b: int, corner: int):
        self.leds = leds
        self.startingFrame = startingFrame
        self.frameDuration = frameDuration
        self.r = r
        self.g = g
        self.b = b
        self.corner = corner

        self.cellDuration = frameDuration / 2

        self.setup()

    def setup(self):
       
        if (self.corner == 0):
            for i in range(3):
                for j in range(3):
                    cell = self.leds[i][j]
                    cell.r = 0
                    cell.g = 0
                    cell.b = 0

                    brightnessFactor = 1
                    distanceFromCorner = i + j
                    if distanceFromCorner == 1:
                        brightnessFactor = 0.6
                    elif distanceFromCorner == 2:
                        brightnessFactor = 0.3
                    elif distanceFromCorner == 3:
                        brightnessFactor = 0.1
                    elif distanceFromCorner == 4:
                        brightnessFactor = 0

                    tCell = LedCell(0, 0, 0, self.r, self.g, self.b)
                    tCell = changeBrightness(tCell, brightnessFactor)

                    cell.tr = tCell.r
                    cell.tg = tCell.g
                    cell.tb = tCell.b

        elif (self.corner == 1):
            for i in range(3):
                for j in range(2, 5):
                    cell = self.leds[i][j]
                    cell.r = 0
                    cell.g = 0
                    cell.b = 0

                    brightnessFactor = 1
                    cornerRow = 0
                    cornerCol = 4
                    distanceFromCorner = abs(i - cornerRow) + abs(j - cornerCol)
                    if distanceFromCorner == 1:
                        brightnessFactor = 0.6
                    elif distanceFromCorner == 2:
                        brightnessFactor = 0.3
                    elif distanceFromCorner == 3:
                        brightnessFactor = 0.1
                    elif distanceFromCorner == 4:
                        brightnessFactor = 0

                    tCell = LedCell(0, 0, 0, self.r, self.g, self.b)
                    tCell = changeBrightness(tCell, brightnessFactor)

                    cell.tr = tCell.r
                    cell.tg = tCell.g
                    cell.tb = tCell.b
    

    def run(self, frame: int):
        for row in self.leds:
            for cell in row:
                flash.run(cell, cell.tr, cell.tg, cell.tb, self.cellDuration, frame)