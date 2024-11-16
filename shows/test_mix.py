from scenes.center_cascade import CenterCascade
from scenes.corner_cascade import CornerCascade
from functions import setup

def testMix1(rows, columns, getStartingFrame, getFrameDuration):
    return [
        CenterCascade(setup.run(rows, columns), getStartingFrame(0), getFrameDuration(1), 255, 0, 0, True),
        CenterCascade(setup.run(rows, columns), getStartingFrame(0), getFrameDuration(1), 0, 255, 0, False),
        CenterCascade(setup.run(rows, columns), getStartingFrame(1), getFrameDuration(1), 0, 255, 0, True),
        CenterCascade(setup.run(rows, columns), getStartingFrame(1), getFrameDuration(1), 0, 0, 255, False),
        CenterCascade(setup.run(rows, columns), getStartingFrame(2), getFrameDuration(1), 0, 0, 255, True),
        CenterCascade(setup.run(rows, columns), getStartingFrame(2), getFrameDuration(1), 255, 0, 0, False),
    ]

def testMix2(rows, columns, getStartingFrame, getFrameDuration):
    return [
        CenterCascade(setup.run(rows, columns), getStartingFrame(0), getFrameDuration(1), 255, 0, 0, True),
        CenterCascade(setup.run(rows, columns), getStartingFrame(.25), getFrameDuration(1), 255, 165, 0, True),
        CenterCascade(setup.run(rows, columns), getStartingFrame(.5), getFrameDuration(1), 165, 255, 0, True),
        CenterCascade(setup.run(rows, columns), getStartingFrame(.75), getFrameDuration(1), 0, 255, 0, True),
        CenterCascade(setup.run(rows, columns), getStartingFrame(1), getFrameDuration(1), 0, 165, 255, True),
        CenterCascade(setup.run(rows, columns), getStartingFrame(1.25), getFrameDuration(1), 0, 0, 255, True),
        CenterCascade(setup.run(rows, columns), getStartingFrame(1.5), getFrameDuration(1), 255, 0, 165, True),
        CenterCascade(setup.run(rows, columns), getStartingFrame(1.75), getFrameDuration(1), 255, 0, 0, True),
    ]

def testMix3(rows, columns, getStartingFrame, getFrameDuration):
    return [
        CornerCascade(setup.run(rows, columns), getStartingFrame(0), getFrameDuration(1), 255, 0, 0, False),
        CornerCascade(setup.run(rows, columns), getStartingFrame(.25), getFrameDuration(1), 0, 255, 0, True),
        CornerCascade(setup.run(rows, columns), getStartingFrame(.5), getFrameDuration(1), 0, 0, 255, False),
    ]

def testMix4(rows, columns, getStartingFrame, getFrameDuration):
    return [
        CenterCascade(setup.run(rows, columns), getStartingFrame(0), getFrameDuration(4), 100, 100, 100, True),
        CornerCascade(setup.run(rows, columns), getStartingFrame(1), getFrameDuration(1), 0, 255, 0, True),
        CornerCascade(setup.run(rows, columns), getStartingFrame(2), getFrameDuration(1), 0, 0, 255, True),
        CornerCascade(setup.run(rows, columns), getStartingFrame(3), getFrameDuration(1), 255, 0, 0, True)
    ]