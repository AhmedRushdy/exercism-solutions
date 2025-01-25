import math

def score(x, y):
    radius = math.sqrt((x ** 2) + (y ** 2))
    if radius > 10:
        return 0
    elif 10 >= radius > 5:
        return 1
    elif 5 >= radius > 1:
        return 5
    elif radius <= 1 or radius >= 0:
        return 10

