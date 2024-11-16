from classes.led import LedCell

def changeBrightness(cell: LedCell, factor: float):

    newCell = LedCell(cell.sI, cell.xI, cell.yI, cell.r, cell.g, cell.b)

    newCell.r = min(255, cell.r * factor)
    newCell.g = min(255, cell.g * factor)
    newCell.b = min(255, cell.b * factor)

    return newCell
