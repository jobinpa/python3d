from vpython import *
from time import *

# size = w/l/h

floor = box(pos=vector(0, -5, 0), size=vector(10, 0.1, 10), color=color.white)
ceiling = box(pos=vector(0, 5, 0), size=vector(10, 0.1, 10), color=color.white)
leftWall = box(pos=vector(-5, 0, 0), size=vector(0.1, 10, 10), color=color.white)
rightWall = box(pos=vector(5, 0, 0), size=vector(0.1, 10, 10), color=color.white)
backWall = box(pos=vector(0, 0, -5), size=vector(10, 10, 0.1), color=color.white)

marble = sphere(radius=0.5, color=color.red)

detalX = 0.1
xPos = 0

while True:
    rate(10)
    xPos = xPos+detalX
    if xPos > 5 or xPos < -5:
        detalX = detalX * -1
    marble.pos = vector(xPos, 0, 0)
