from scenes.center_cascade import CenterCascade
from scenes.corner_cascade import CornerCascade
from scenes.corner_flash import CornerFlash
from scenes.cell_blink import CellBlink
from scenes.side_cascade import SideCascade
from scenes.single_line_cascade import SingleLineCascade
from scenes.center_cascade_rainbow import CenterCascadeRainbow
from scenes.partial_flash import PartialFlash
from scenes.fade import Fade
from functions import setup
from classes.scene import Scene
from typing import List, Callable


def curiousFish(rows, columns, getStartingFrame, getFrameDuration):

    frameOffset = 4

    startingScenes = [
        CenterCascade(setup.run(rows, columns), getStartingFrame(0), getFrameDuration(1), 255, 0, 0, False),
        CenterCascade(setup.run(rows, columns), getStartingFrame(1), getFrameDuration(1), 255, 165, 0, False),
        CenterCascade(setup.run(rows, columns), getStartingFrame(2), getFrameDuration(1), 255, 255, 0, False),
        CornerCascade(setup.run(rows, columns), getStartingFrame(3), getFrameDuration(1), 0, 0, 255, False),
    ]

    # region intro

    intoLineScenes = []

    def introEndCallback():
        print("Ending scenes")
        for scene in intoLineScenes:
            scene.stop()

    introScenes = [
        Fade(setup.run(rows, columns), getStartingFrame(frameOffset + 1), getFrameDuration(14.5), 0, 0, 75),
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(frameOffset + 9), getFrameDuration(1.5), 255, 0, 0, 1, 4),
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(frameOffset + 9.25), getFrameDuration(1.5), 255, 0, 0, 1, 2),
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(frameOffset + 11), getFrameDuration(1.5), 255, 0, 0, 1, 3),
        SingleLineCascade(setup.run(rows, columns), getStartingFrame(frameOffset + 11.25), getFrameDuration(1.5), 255, 0, 0, 1, 1),
        SideCascade(setup.run(rows, columns), getStartingFrame(frameOffset + 12.75), getFrameDuration(1.5), 255, 0, 0, 0),
        CornerCascade(setup.run(rows, columns), getStartingFrame(frameOffset + 14.25), getFrameDuration(1), 255, 0, 0, False),
        # CornerCascade(setup.run(rows, columns), getStartingFrame(frameOffset + 15.25), getFrameDuration(1), 255, 0, 0, False),

        # CenterCascadeRainbow(setup.run(rows, columns), getStartingFrame(frameOffset + 15.5), getFrameDuration(1), False, introEndCallback),
        CenterCascade(setup.run(rows, columns), getStartingFrame(frameOffset + 15.5), getFrameDuration(1), 255, 0, 0, False, introEndCallback),
        CenterCascade(setup.run(rows, columns), getStartingFrame(frameOffset + 15.7), getFrameDuration(1), 0, 255, 0, False),
        CenterCascade(setup.run(rows, columns), getStartingFrame(frameOffset + 15.9), getFrameDuration(1), 0, 0, 255, False),
    ]



    for i in range(13):
        offset = i + 3
        intoLineScenes += [
            SingleLineCascade(setup.run(rows, columns), getStartingFrame(frameOffset + 0 + offset), getFrameDuration(2), 0, 0, 50, 0, (i + 3) % 6),
            SingleLineCascade(setup.run(rows, columns), getStartingFrame(frameOffset + 0 + offset - .5), getFrameDuration(2), 0, 0, 50, 0, (i + 1) % 6),
        ]

    introScenes += intoLineScenes

    frameOffset += 17

    for i in range(20):
        introScenes.append(
            CornerCascade(setup.run(rows, columns), getStartingFrame(frameOffset + i), getFrameDuration(1), 0, 0, 255, False),
        )


    # end region

    # region into two

    introTwoScenes = []
    

    bars = 14

    for i in range(bars):

        barOffest = i * 4

        introTwoScenes += [
            PartialFlash(setup.run(rows, columns), getStartingFrame(frameOffset + barOffest + 1), getFrameDuration(.5), 255, 255, 255, 0, 0, 6, 5),
            PartialFlash(setup.run(rows, columns), getStartingFrame(frameOffset + barOffest + 2.75), getFrameDuration(.5), 255, 255, 255, 0, 0, 3, 5),
            PartialFlash(setup.run(rows, columns), getStartingFrame(frameOffset + barOffest + 3), getFrameDuration(.75), 255, 255, 255, 3, 0, 6, 5),
        ]



    # end region



    # region outro

    bars = 16

    noteDuration = 1

    # Descending note order
    # x is row y is column

    # d4
    d4x = 2
    d4y = 1

    d4r = 255
    d4g = 255
    d4b = 255 #0

    # c4
    c4x = 2
    c4y = 2

    c4r = 255 #0
    c4g = 255
    c4b = 255 #0

    #a#3
    aSharp3x = 3
    aSharp3y = 1

    aSharp3r = 255
    aSharp3g = 255
    aSharp3b = 255 #0

    # g#3
    gSharp3x = 3
    gSharp3y = 2

    gSharp3r = 255
    gSharp3g = 255
    gSharp3b = 255

    # g3
    g3x = 3
    g3y = 3

    g3r = 255 #0
    g3g = 255 #0
    g3b = 255

    # f3
    f3x = 4
    f3y = 1

    f3r = 255 #0
    f3g = 255
    f3b = 255

    # d#3
    dSharp3x = 4
    dSharp3y = 2

    dSharp3r = 255
    dSharp3g = 255 #0
    dSharp3b = 255 #0

    # d3
    d3x = 4
    d3y = 3

    d3r = 255
    d3g = 255 #0
    d3b = 255


    noteScenes = []

    for i in range(2):

        sequenceOffset = i * 32

        noteSequenceScenes = [
            # a#3
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 1 + sequenceOffset), getFrameDuration(noteDuration), aSharp3r, aSharp3g, aSharp3b, aSharp3x, aSharp3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 25 + sequenceOffset), getFrameDuration(noteDuration), aSharp3r, aSharp3g, aSharp3b, aSharp3x, aSharp3y),

            # g#3
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 5 + sequenceOffset), getFrameDuration(noteDuration), gSharp3r, gSharp3g, gSharp3b, gSharp3x, gSharp3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 9 + sequenceOffset), getFrameDuration(noteDuration), gSharp3r, gSharp3g, gSharp3b, gSharp3x, gSharp3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 17 + sequenceOffset), getFrameDuration(noteDuration), gSharp3r, gSharp3g, gSharp3b, gSharp3x, gSharp3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 29 + sequenceOffset), getFrameDuration(noteDuration), gSharp3r, gSharp3g, gSharp3b, gSharp3x, gSharp3y),

            # d#3
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 1.5 + sequenceOffset), getFrameDuration(noteDuration), dSharp3r, dSharp3g, dSharp3b, dSharp3x, dSharp3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 13.25 + sequenceOffset), getFrameDuration(noteDuration), dSharp3r, dSharp3g, dSharp3b, dSharp3x, dSharp3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 21.25 + sequenceOffset), getFrameDuration(noteDuration), dSharp3r, dSharp3g, dSharp3b, dSharp3x, dSharp3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 25.5 + sequenceOffset), getFrameDuration(noteDuration), dSharp3r, dSharp3g, dSharp3b, dSharp3x, dSharp3y),

            # d4
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 1.875 + sequenceOffset), getFrameDuration(noteDuration), d4r, d4g, d4b, d4x, d4y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 17.875 + sequenceOffset), getFrameDuration(noteDuration), d4r, d4g, d4b, d4x, d4y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 25.875 + sequenceOffset), getFrameDuration(noteDuration), d4r, d4g, d4b, d4x, d4y),

            # g3
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 2.5 + sequenceOffset), getFrameDuration(noteDuration), g3r, g3g, g3b, g3x, g3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 5.625 + sequenceOffset), getFrameDuration(noteDuration), g3r, g3g, g3b, g3x, g3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 10.5 + sequenceOffset), getFrameDuration(noteDuration), g3r, g3g, g3b, g3x, g3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 18.5 + sequenceOffset), getFrameDuration(noteDuration), g3r, g3g, g3b, g3x, g3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 26.5 + sequenceOffset), getFrameDuration(noteDuration), g3r, g3g, g3b, g3x, g3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 29.625 + sequenceOffset), getFrameDuration(noteDuration), g3r, g3g, g3b, g3x, g3y),

            # c4
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 9.825 + sequenceOffset), getFrameDuration(noteDuration), c4r, c4g, c4b, c4x, c4y),

            # d3
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 9.5 + sequenceOffset), getFrameDuration(noteDuration), d3r, d3g, d3b, d3x, d3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 17.5 + sequenceOffset), getFrameDuration(noteDuration), d3r, d3g, d3b, d3x, d3y),

            # f3
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 12.875 + sequenceOffset), getFrameDuration(noteDuration), f3r, f3g, f3b, f3x, f3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 13.625 + sequenceOffset), getFrameDuration(noteDuration), f3r, f3g, f3b, f3x, f3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 20.875 + sequenceOffset), getFrameDuration(noteDuration), f3r, f3g, f3b, f3x, f3y),
            CellBlink(setup.run(rows, columns), getStartingFrame(frameOffset + 21.625 + sequenceOffset), getFrameDuration(noteDuration), f3r, f3g, f3b, f3x, f3y),
        ]

        noteScenes.extend(noteSequenceScenes)


    cornerScenes = []

    for i in range(bars):
        barOffset = i * 4

        r = 0
        g = 0
        b = 0

        match i % 4:
            case 0:
                b = 255
            case 1:
                r = 100
                b = 200
            case 2:
                b = 255
            case 3:
                b = 100
                r = 200


        cornerScenes.append(
            CenterCascade(setup.run(rows, columns), getStartingFrame(frameOffset + 0+ barOffset), getFrameDuration(1), r, g, b, False),
        )

    bassScenes = []
    bassLength = .5

    for i in range(bars):

        barOffset = i * 4

        barScenes = [
            CornerFlash(setup.run(rows, columns), getStartingFrame(frameOffset + 0 + barOffset), getFrameDuration(bassLength), 0, 255, 255, 0),
            CornerFlash(setup.run(rows, columns), getStartingFrame(frameOffset + 1.75 + barOffset), getFrameDuration(bassLength), 0, 255, 255, 0),
            CornerFlash(setup.run(rows, columns), getStartingFrame(frameOffset + 2 + barOffset), getFrameDuration(bassLength), 0, 255, 255, 0),
            CornerFlash(setup.run(rows, columns), getStartingFrame(frameOffset + 3.75 + barOffset), getFrameDuration(bassLength), 0, 255, 255, 0),
        ]

        bassScenes.extend(barScenes)

    snareScenes = []
    snareLength = .5
    for i in range(bars):
        barOffset = i * 4

        barScenes = [
            CornerFlash(setup.run(rows, columns), getStartingFrame(frameOffset + 1 + barOffset), getFrameDuration(snareLength), 255, 0, 255, 1),
            CornerFlash(setup.run(rows, columns), getStartingFrame(frameOffset + 3 + barOffset), getFrameDuration(snareLength), 255, 0, 255, 1),
            CornerFlash(setup.run(rows, columns), getStartingFrame(frameOffset + 3.25 + barOffset), getFrameDuration(snareLength), 255, 0, 255, 1),
        ]

        snareScenes.extend(barScenes)

    clapScenes = []
    clapLength = 1
    for i in range(int(bars)):
        barOffset = i * 4

        leftR = 0
        leftG = 0
        leftB = 0
        rightR = 0
        rightG = 0
        rightB = 0

        leftReverse = False
        rightReverse = False

        leftSide = 0
        rightSide = 0

        match i % 4:
            case 0:
                leftR = 155
                rightB = 155
                leftSide = 0
                rightSide = 2
            case 1:
                leftB = 155
                rightR = 155
                rightReverse = True
                leftSide = 1
                rightSide = 3
            case 2:
                leftR = 155
                rightB = 155
                leftReverse = True
                leftSide = 2
                rightSide = 1
            case 3:
                leftB = 155
                rightR = 155
                rightReverse = True
                leftSide = 3
                rightSide = 0

        barScenes = [
            SideCascade(setup.run(rows, columns), getStartingFrame(frameOffset + 2.5 + barOffset), getFrameDuration(clapLength), leftR, leftG, leftB, leftSide),
            SideCascade(setup.run(rows, columns), getStartingFrame(frameOffset + 2.75 + barOffset), getFrameDuration(clapLength), rightR, rightG, rightB, rightSide),
        ]

        clapScenes.extend(barScenes)

    outroScenes = noteScenes + cornerScenes + clapScenes

    # end region

    return startingScenes + introTwoScenes + introScenes

    # return startingScenes + outroScenes