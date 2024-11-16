def mixColors(color1, color2):
    """Mix two colors by averaging their RGB values."""
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return (int((r1 + r2) / 2), int((g1 + g2) / 2), int((b1 + b2) / 2))