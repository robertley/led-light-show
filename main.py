#include all neccessary packages to get LEDs to work with Raspberry Pi
import time
import board
import neopixel
from functions import setup
from scenes import blink
from scenes.center_cascade import CenterCascade
from scenes.corner_cascade import CornerCascade
from scenes.corner_flash import CornerFlash
from scenes.single_line_cascade import SingleLineCascade
from scenes.quick_rainbow_flash import QuickRainbowFlash
from scenes.center_cascade_rainbow import CenterCascadeRainbow
from scenes.partial_flash import PartialFlash
from scenes.fade import Fade
from classes.scene import Scene
from classes.frame import Frame
from typing import List
from shows.test_mix import testMix1, testMix2, testMix3, testMix4
from shows.curious_fish import curiousFish
from shows.single_line_test import singleLineTest

numLeds: int = 55
rows: int = 6
columns: int = 5

neo = neopixel.NeoPixel(board.D18, numLeds, brightness=.3, auto_write=False)

bpm = 96
# beat length in miliseconds
beatLength = 60000 / bpm
frameRate = 10
framesPerBeat = beatLength / frameRate

print("Blinking to the beat at %d BPM" % bpm)



leds = setup.run(rows, columns)

def getStartingFrame(beatNum: int):
    global framesPerBeat
    return beatNum * framesPerBeat

def getFrameDuration(beatAmt: int):
    global framesPerBeat
    return framesPerBeat * beatAmt

# scenes: List[Scene] = curiousFish(rows, columns, getStartingFrame, getFrameDuration)
scenes: List[Scene]

def createScenes():
    global scenes
    # scenes = [
    #     # CenterCascadeRainbow(setup.run(rows, columns), getStartingFrame(0), getFrameDuration(2), False),

    #     CenterCascade(setup.run(rows, columns), getStartingFrame(0), getFrameDuration(1), 255, 0, 0, False),
    #     CenterCascade(setup.run(rows, columns), getStartingFrame(0.15), getFrameDuration(1), 0, 255, 0, False),
    #     CenterCascade(setup.run(rows, columns), getStartingFrame(.3), getFrameDuration(1), 0, 0, 255, False),
    # ]
    # scenes = [
    #     PartialFlash(setup.run(rows, columns), getStartingFrame(0), getFrameDuration(.5), 255, 255, 255, 0, 0, 3, 5),
    #     PartialFlash(setup.run(rows, columns), getStartingFrame(.5), getFrameDuration(1), 255, 255, 255, 3, 0, 6, 5),
    # ]
    scenes = curiousFish(rows, columns, getStartingFrame, getFrameDuration)
    

createScenes()

beatMilis = 0
frameNum = 0
beatNum = 0
totalFrames = 0
startingMilis = 0

latestStartingFrame = 0
latestStartingFrameScenes = []
for scene in scenes:
    startingFrame = max(latestStartingFrame, scene.startingFrame + scene.frameDuration)

    if startingFrame == latestStartingFrame:
        latestStartingFrameScenes.append(scene)

    if startingFrame > latestStartingFrame:
        latestStartingFrameScenes = [scene]
        latestStartingFrame = startingFrame

for scene in latestStartingFrameScenes:
    totalFrames = max(totalFrames, scene.startingFrame + scene.frameDuration)

# totalFrames = getFrameDuration(4)

print("Total frames: %d" % totalFrames)
print("Beat length: %f" % beatLength)
print("Frame rate: %f" % frameRate)
print("Frames per beat: %f" % framesPerBeat)

def nextFrame():
    global frameRate
    currentMilis = int(round(time.time() * 1000))
    newFrame = False
    if currentMilis > startingMilis + (frameNum * frameRate):
        newFrame = True
    
    return Frame(currentMilis, newFrame)

# prompt user to press enter to start
enter = input("Press Enter to start")

while True:

    frame = nextFrame()
    if (startingMilis == 0):
        startingMilis = frame.milis

    if not frame.newFrame:
        continue

    frameNum += 1

    # do scenes
    for scene in scenes:
        if frameNum <= scene.startingFrame:
            continue
        if frameNum > scene.startingFrame + scene.frameDuration:
            continue

        scene.run(frameNum - scene.startingFrame)


    drawLeds = setup.run(rows, columns)

    for scene in scenes:
        if frameNum >= scene.startingFrame and frameNum <= scene.startingFrame + scene.frameDuration:
            
            for row in scene.leds:
                for cell in row:
                    drawCell = drawLeds[cell.xI][cell.yI]
                    drawCell.r = min(255, drawCell.r + cell.r)
                    drawCell.g = min(255, drawCell.g + cell.g)
                    drawCell.b = min(255, drawCell.b + cell.b)
    
    for row in drawLeds:
        for cell in row:
            neo[cell.sI] = (int(cell.r), int(cell.g), int(cell.b))

    # check if new beat
    if frame.milis > beatMilis:
        beatMilis = frame.milis + beatLength
        beatNum += 1
        # print("startingMilis: %d" % startingMilis)
        # print("frame.milis: %d" % frame.milis)
        # print("Beat: %d" % (beatNum - 5))


    neo.show()

    # reset show if we reach the end
    if frameNum >= totalFrames:
        frameNum = 0
        startingMilis = 0
        createScenes()
        beatNum = 0
        
        # for scene in scenes:
        #     scene.setup()
        # print("Reset")

    


    # print("Frame: %d nextMilis: %d" % (frame, nextMilis))