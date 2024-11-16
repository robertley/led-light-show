from classes.led import LedCell
from classes.scene import Scene
from typing import List
from functions import flash
from math import floor

class QuickRainbowFlash(Scene):

    def __init__(self, leds: List[List[LedCell]], startingFrame: int, frameDuration: int):
        self.leds = leds
        self.startingFrame = startingFrame
        self.frameDuration = frameDuration

        self.cellDuration = frameDuration / 2
        self.cellDelays = []

        self.setup()

    def setup(self):
       for i in range(len(self.leds)):
            for j in range(len(self.leds[i])):
                cell = self.leds[i][j]
                cell.r = 0
                cell.g = 0
                cell.b = 0

    

    def run(self, frame: int):

        skipFrames = 10

        if frame % skipFrames != 0:
            return

        # skipFrames = 2
        # 2, 4, 6, 8, 10 ...

        # skipFrames = 3
        # 3, 6, 9, 12, 15 ...

        colors = 6

        whiteFrames = []
        colorFrames = []

        for i in range(colors * 2):
            if i % 2 == 0:
                whiteFrames.append(skipFrames * i)
            else:
                colorFrames.append(skipFrames * i)

        frameMod = frame % (skipFrames * colors * 2)

        for row in self.leds:
            for cell in row:

                if frameMod in whiteFrames:
                    cell.r = 100
                    cell.g = 100
                    cell.b = 100
                elif frameMod == colorFrames[0]:
                    cell.r = 255
                    cell.g = 0
                    cell.b = 0
                elif frameMod == colorFrames[1]:
                    cell.r = 255
                    cell.g = 255
                    cell.b = 0
                elif frameMod == colorFrames[2]:
                    cell.r = 0
                    cell.g = 255
                    cell.b = 0
                elif frameMod == colorFrames[3]:
                    cell.r = 0
                    cell.g = 255
                    cell.b = 255
                elif frameMod == colorFrames[4]:
                    cell.r = 0
                    cell.g = 0
                    cell.b = 255
                elif frameMod == colorFrames[5]:
                    cell.r = 255
                    cell.g = 0
                    cell.b = 255