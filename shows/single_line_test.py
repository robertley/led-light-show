from scenes.single_line_cascade import SingleLineCascade
from functions import setup

def singleLineTest(rows, columns, getStartingFrame, getFrameDuration):
    return [
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(0), getFrameDuration(2), r=0, g=0, b=255, side=0, lineIndex=0),
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(.25), getFrameDuration(2), r=0, g=0, b=255, side=0, lineIndex=1),
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(.5), getFrameDuration(2), r=0, g=0, b=255, side=0, lineIndex=2),
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(.75), getFrameDuration(2), r=0, g=0, b=255, side=0, lineIndex=3),
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(1), getFrameDuration(2), r=0, g=0, b=255, side=0, lineIndex=4),
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(1.25), getFrameDuration(2), r=0, g=0, b=255, side=0, lineIndex=5),
        
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(0), getFrameDuration(2), r=255, g=0, b=0, side=2, lineIndex=0),
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(.25), getFrameDuration(2), r=255, g=0, b=0, side=2, lineIndex=1),
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(.5), getFrameDuration(2), r=255, g=0, b=0, side=2, lineIndex=2),
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(.75), getFrameDuration(2), r=255, g=0, b=0, side=2, lineIndex=3),
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(1), getFrameDuration(2), r=255, g=0, b=0, side=2, lineIndex=4),
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(1.25), getFrameDuration(2), r=255, g=0, b=0, side=2, lineIndex=5),
    ]