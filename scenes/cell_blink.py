import time
import neopixel
from classes.led import LedCell
from classes.scene import Scene
from typing import List
from functions import flash

class CellBlink(Scene):

    def __init__(self, leds, startingFrame: int, frameDuration: int, r: int, g: int, b: int, x: int, y: int):
        self.leds = leds
        self.startingFrame = startingFrame
        self.frameDuration = frameDuration
        self.r = r
        self.g = g
        self.b = b
        self.x = x
        self.y = y

        self.cellDuration = frameDuration / 2
        self.cellDelays = []

        self.setup()

    def setup(self):
        cell = self.leds[self.x][self.y]
        cell.r = 0
        cell.g = 0
        cell.b = 0
    

    def run(self, frame: int):
        cell = self.leds[self.x][self.y]
        flash.run(cell, self.r, self.g, self.b, self.cellDuration, frame)
                    
                    
        


# def centerCascade(neo: neopixel, leds: List[List[LedCell]], beats: int, r: int, g: int, b: int):

#     for row in leds:
#         for cell in row:
#             neo[cell.sI] = (0, 0, 0)