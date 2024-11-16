from classes.led import LedCell

def run(rows, columns):

    leds = []

    for i in range(rows):
        row = []
        for j in range(columns):
            yIndex = j
            if i % 2 == 1:
                yIndex = columns - 1 - j
            # TODO this is not generic for any number of rows/columns
            sI = (i * 9) + (yIndex * 2) + 1
            row.insert(j, LedCell(sI, i, j, 0, 0, 0))

        leds.insert(i, row)

    return leds
    # for (int i = 0; i < NUM_LEDS; i++) {
    #     leds[i] = CRGB(0, 0, 0);
    # }

    # for (int i = 0; i < rows; i++) {
    #     for (int j = 0; j < columns; j++) {
    #     int yIndex = j;

    #   if (i % 2 == 1) {
    #     yIndex = columns - 1 - j;
    #   }
    #   ledCell cell;
    #   cell.red = 0;
    #   cell.green = 0;
    #   cell.blue = 0;
    #   cell.stripIndex = (i * 9) + (yIndex * 2) + 1;
    #   cell.array2dX = i;
    #   cell.array2dY = j;
    #   cells[i][j] = cell;
    # }
#   }