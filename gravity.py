import tkinter as tk
import time

GRAVITY = 500000
SQUARE_SIZE = 50
MAX_VELOCITY_X = 1500
MAX_VELOCITY_Y = 2500
DECELERATION = 130000#Deceleration of the X axis velocity
VELOCITY_HISTORY = 100

velocityXHistory = []
for i in range(VELOCITY_HISTORY):
    velocityXHistory.append(0)

velocityYHistory = []
for i in range(VELOCITY_HISTORY):
    velocityYHistory.append(0)

windowSizeX = 600
windowSizeY = 600
x, y = 800, 500
lastFrameX, lastFrameY = x, y
velocityX, velocityY = 0, 0

root = tk.Tk()
root.resizable(True, True)
canvas = tk.Canvas(master=root, width=8000, height=8000, bg="black")
root.geometry(f"{windowSizeX}x{windowSizeY}")
canvas.pack()

def clamp(my_value, min_value, max_value):
    return max(min(my_value, max_value), min_value)

def positionShenanigans(dt):
    global x, y
    x += velocityX * dt
    y += velocityY * dt
    x = clamp(x, root.winfo_x(), root.winfo_x()+windowSizeX-SQUARE_SIZE)
    y = clamp(y, root.winfo_y(), root.winfo_y()+windowSizeY-SQUARE_SIZE)

def velocityStuff(dt):
    global x, y, velocityX, velocityY

    velocityXHistory.pop(0)
    velocityXHistory.append((x - lastFrameX)/dt)
    velocityX = sum(velocityXHistory)/VELOCITY_HISTORY
    if(velocityX > 0):
        if(velocityX < DECELERATION*dt):
            velocityX = 0
        else:
            velocityX -= DECELERATION*dt
    elif(velocityX < 0):
        if(velocityX > -DECELERATION*dt):
            velocityX = 0
        else:
            velocityX += DECELERATION*dt
    velocityX = clamp(velocityX, -MAX_VELOCITY_X, MAX_VELOCITY_X)

    velocityYHistory.pop(0)
    velocityYHistory.append((y - lastFrameY)/dt)
    velocityY = sum(velocityYHistory)/VELOCITY_HISTORY
    velocityY += GRAVITY*dt
    velocityY = clamp(velocityY, -MAX_VELOCITY_Y, MAX_VELOCITY_Y)

lastFrameTime = time.time()
while True:
    windowSizeX = root.winfo_width()
    windowSizeY = root.winfo_height()
    dt = time.time() - lastFrameTime
    lastFrameTime = time.time()
    positionShenanigans(dt)
    velocityStuff(dt)
    lastFrameX = x
    lastFrameY = y
    canvas.delete("all")
    canvas.create_rectangle(x-root.winfo_x(), y-root.winfo_y(), x-root.winfo_x()+SQUARE_SIZE, y-root.winfo_y()+SQUARE_SIZE, fill="white")
    canvas.update()