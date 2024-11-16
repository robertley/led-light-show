class LedCell:

    def __init__(self, sI, xI, yI, r, g, b):
        self.sI = sI
        self.xI = xI
        self.yI = yI
        self.r = r
        self.g = g
        self.b = b
        self.delay = 0
        self.tr = 0
        self.tg = 0
        self.tb = 0

    sI: int
    xI: int
    yI: int
    r: int
    g: int
    b: int

    #scene attributes
    delay: int
    tr: int
    tg: int
    tb: int

    def reset(self):
        self.r = 0
        self.g = 0
        self.b = 0