from classes.led import LedCell
from classes.scene import Scene
from typing import List
from functions import flash
from functions import fade

class Fade(Scene):

    def __init__(self, leds, startingFrame: int, frameDuration: int, r: int, g: int, b: int):
        self.leds = leds
        self.startingFrame = startingFrame
        self.frameDuration = frameDuration
        self.r = r
        self.g = g
        self.b = b

        self.setup()

    def setup(self):
        None
    

    def run(self, frame: int):
        for row in self.leds:
            for cell in row:
                if frame == self.frameDuration:
                    cell.reset()
                    continue

                fade.run(cell, self.r, self.g, self.b, self.frameDuration)
        

                    
                    
        


# def centerCascade(neo: neopixel, leds: List[List[LedCell]], beats: int, r: int, g: int, b: int):

#     for row in leds:
#         for cell in row:
#             neo[cell.sI] = (0, 0, 0)