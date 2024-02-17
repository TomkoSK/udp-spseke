import tkinter as tk
import time
import random
from randomcolor import randcolor

canvas = tk.Canvas(height = 600, width = 600)
canvas.pack()


currentTime = time.time()
corners = [[40, 40], [560, 560]]
speeds = []
squarePositions = []
colors = []
squareSize = 50
for i in range(1):
    speeds.append([random.randint(5, 10), random.randint(5, 10)])
    squarePositions.append([random.randint(100, 500), random.randint(100, 500)])
    colors.append(randcolor())

def clamp(n, min, max): 
    if n < min: 
        return min
    elif n > max: 
        return max
    else: 
        return n

while True:
    canvas.delete("all")
    canvas.create_rectangle(corners[0], corners[1], outline="black", width = 3)
    for i in range(len(squarePositions)):
        squarePositions[i][0] += speeds[i][0]
        squarePositions[i][1] += speeds[i][1]
        if(squarePositions[i][0]+squareSize > corners[1][0] or squarePositions[i][0] < corners[0][0]):
            corners[0][0] += 5
            corners[1][0] -= 5
            squarePositions[i][0] = clamp(squarePositions[i][0], corners[0][0], corners[1][0]-squareSize)
            speeds[i][0] = -speeds[i][0]
        if(squarePositions[i][1]+squareSize > corners[1][1] or squarePositions[i][1] < corners[0][1]):
            corners[0][1] += 5
            corners[1][1] -= 5
            speeds[i][1] = -speeds[i][1]
            squarePositions[i][1] = clamp(squarePositions[i][1], corners[0][1], corners[1][1]-squareSize)
        canvas.create_rectangle(squarePositions[i][0], squarePositions[i][1], squarePositions[i][0]+squareSize, squarePositions[i][1]+squareSize, fill=colors[i])
    canvas.update()
    time.sleep(0.02)

tk.mainloop()