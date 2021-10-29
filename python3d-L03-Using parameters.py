from vpython import *
from time import *

# Parameters
mRadius = 0.75
wallThickness = 0.1
roomWidth = 10
roomDepth = 5
roomHeight = 10

floor = box(pos=vector(0, -roomHeight/2, 0), size=vector(roomWidth, wallThickness, roomDepth), color=color.white)
ceiling = box(pos=vector(0, roomHeight/2, 0), size=vector(roomWidth, wallThickness, roomDepth), color=color.white)
leftWall = box(pos=vector(-roomWidth/2, 0, 0), size=vector(wallThickness, roomHeight, roomDepth), color=color.white)
rightWall = box(pos=vector(roomWidth/2, 0, 0), size=vector(wallThickness, roomHeight, roomDepth), color=color.white)
backWall = box(pos=vector(0, 0, -roomDepth/2), size=vector(roomWidth, roomHeight, wallThickness), color=color.white)

marble = sphere(radius=mRadius, color=color.red)

detalX = 0.1
xPos = 0

while True:
    rate(10)
    xPos = xPos+detalX
    if xPos > roomWidth/2 or xPos < -roomWidth/2:
        detalX = detalX * -1
    marble.pos = vector(xPos, 0, 0)
