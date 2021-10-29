from vpython import *
from time import *

floor = box( pos=vector(0, -5, 0), color=color.white, length=10, height=0.1, width=10)
leftWall = box( pos=vector(-5, 0, 0), color=color.white, length=0.1, height=10, width=10)
ceiling = box( pos=vector(0, 5, 0), color=color.white, length=10, height=0.1, width=10)
rightWall = box( pos=vector(5, 0, 0), color=color.white, length=0.1, height=10, width=10)
backWall = box( pos=vector(0, 0, -5), color=color.white, length=10, height=10, width=0.1)

marble = sphere(radius=0.5, color=color.red)

detalX = 0.1
xPos = 0

while True:
    rate(10)
    xPos = xPos+detalX
    if xPos > 5 or xPos < -5:
        detalX = detalX * -1
    marble.pos = vector(xPos, 0, 0)
