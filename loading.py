import tkinter as tk
import time
import math

canvas = tk.Canvas(height = 600, width = 600)

canvas.pack()

angle = 0

centerX = 300
centerY = 300
radius = 100

radiuses = []
speeds = []
angles = []

for i in range(8):
    radiuses.append(30+i*15)
    speeds.append(2+i*2)
    angles.append(0)

while(True):
    canvas.delete("all")
    for i in range(8):
        radAngle = math.radians(angles[i])
        x = centerX+radiuses[i]*math.cos(radAngle)
        y = centerY+radiuses[i]*math.sin(radAngle)
        canvas.create_rectangle(x,y,x+15,y+15, fill="orange")
        angles[i] += speeds[i]
    time.sleep(0.02)
    canvas.update()