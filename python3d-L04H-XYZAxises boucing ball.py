from random import randint
from vpython import *
from time import *

# Parameters
mRadius = 0.75
mMaxVelocity = 1
wallThickness = 1.5
roomWidth = 10
roomDepth = 5
roomHeight = 10

floor = box(pos=vector(0, -roomHeight/2, 0), size=vector(roomWidth + wallThickness, wallThickness, roomDepth), color=color.white)
ceiling = box(pos=vector(0, roomHeight/2, 0), size=vector(roomWidth + wallThickness, wallThickness, roomDepth), color=color.white)
leftWall = box(pos=vector(-roomWidth/2, 0, 0), size=vector(wallThickness, roomHeight, roomDepth), color=color.white)
rightWall = box(pos=vector(roomWidth/2, 0, 0), size=vector(wallThickness, roomHeight, roomDepth), color=color.white)
backWall = box(pos=vector(0, 0, -roomDepth/2), size=vector(roomWidth, roomHeight, wallThickness), color=color.white)

marble = sphere(radius=mRadius, color=color.red)

deltaX = randint(0, int(mMaxVelocity / 0.1)) * 0.1
deltaY = randint(0, int(mMaxVelocity / 0.1)) * 0.1
deltaZ = randint(0, int(mMaxVelocity / 0.1)) * 0.1

xPos = 0
yPos = 0
zPos = 0

leftBoundary = (-roomWidth + wallThickness) / 2
rightBoundary = (roomWidth - wallThickness) / 2
bottomBoundary = (-roomHeight + wallThickness) / 2
topBoundary = (roomHeight - wallThickness) / 2
backBoundary = (-roomDepth + wallThickness) / 2
frontBoundary = (roomDepth - wallThickness) / 2

while True:
    rate(10)

    xPos = xPos + deltaX
    yPos = yPos + deltaY
    zPos = zPos + deltaZ

    # Left and right wall collisions
    if xPos - mRadius < leftBoundary:
        xPos = leftBoundary + mRadius
        deltaX = deltaX * -1
    elif xPos + mRadius > rightBoundary:
        xPos = rightBoundary - mRadius
        deltaX = deltaX * -1
    
    # Floor and ceiling colisions
    if yPos - mRadius < bottomBoundary:
        yPos = bottomBoundary + mRadius
        deltaY = deltaY * -1
    elif yPos + mRadius > topBoundary:
        yPos = topBoundary - mRadius
        deltaY = deltaY * -1

    # Back and front wall colisions
    if zPos - mRadius < backBoundary:
        zPos = backBoundary + mRadius
        deltaZ = deltaZ * -1
    elif zPos + mRadius > frontBoundary:
        zPos = frontBoundary - mRadius
        deltaZ = deltaZ * -1

    marble.pos = vector(xPos, yPos, zPos)
