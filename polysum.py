import math

def polysum(n, s):
    perimeter = n*s
    area = (0.25*n*s**2) / math.tan(math.pi/n)

    return round(area + perimeter**2, 4)
