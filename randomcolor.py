import random

def randcolor():
    bgString = "#"
    for i in range(6):
        bgColor = hex(random.randint(0, 15))
        bgColor = bgColor[2]
        bgString += bgColor
    return bgString