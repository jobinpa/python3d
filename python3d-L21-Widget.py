from random import randint, randrange, uniform
from typing_extensions import runtime
from vpython import *
from time import *

# Parameters
mRadius = 0.75
mMaxVelocity = 0.5
wallThickness = 1.5
roomWidth = 10
roomDepth = 5
roomHeight = 10
baseSpeed = 5

# Constants
global GRAY
GRAY = vector(128, 128, 128)

# Global variables
isRunning = False
marbleScale = 1
marbleColor = color.red
marbleOpacity = 1
speedMultiplicator = 1

# Widgets
# https://www.glowscript.org/docs/VPythonDocs/controls.html


def onIsRunningChanged(x):
    global isRunning
    isRunning = x.checked


def onMarbleOpacityChanged(x):
    global marbleOpacity
    marbleOpacity = x.value


def onMarbleScaleChanged(x):
    global marbleScale
    marbleScale = 2 if x.checked else 1


def onMarbleColorChanged(x):
    global marbleColor, redButton, greenButton, blueButton
    marbleColor = x.background
    redButton.color = color.black if x == redButton else GRAY
    greenButton.color = color.black if x == greenButton else GRAY
    blueButton.color = color.black if x == blueButton else GRAY


def onAnimationSpeedChanged(x):
    global speedMultiplicator
    speedMultiplicator = int(x.selected)


redButton = button(text='Red', bind=onMarbleColorChanged, color=color.black if marbleColor == color.red else GRAY, background=color.red, disabled=False)
greenButton = button(text='Green', bind=onMarbleColorChanged, color=color.black if marbleColor == color.green else GRAY, background=color.green, disabled=False)
blueButton = button(text='Blue', bind=onMarbleColorChanged, color=color.black if marbleColor == color.blue else GRAY, background=color.blue, disabled=False)
scene.append_to_caption('\n\n')  # Add two new lines after last button

isRunningRadio = radio(text='Run', bind=onIsRunningChanged, checked=isRunning, disabled=False)
scene.append_to_caption('   ')  # Add whitespaces after radio

bigMarbleCheckbox = checkbox(text='Big marble', bind=onMarbleScaleChanged, checked=marbleScale > 1, disabled=False)
scene.append_to_caption('   ')

wtext(text='Speed: ')
speedMenu = menu(bind=onAnimationSpeedChanged, disabled=False,
                 choices=['1', '2', '3', '4', '5'], selected=str(speedMultiplicator))
scene.append_to_caption('\n\n')

wtext(text='Marble opacity:')
scene.append_to_caption('\n\n')
opacitySlidder = slider(text='Opacity', bind=onMarbleOpacityChanged, vertical=False, min=0, max=1,
                        value=marbleOpacity, step=0.01, disable=False)
scene.append_to_caption('\n\n')

floor = box(pos=vector(0, -roomHeight/2, 0), size=vector(roomWidth + wallThickness, wallThickness, roomDepth), color=color.white)
ceiling = box(pos=vector(0, roomHeight/2, 0), size=vector(roomWidth + wallThickness, wallThickness, roomDepth), color=color.white)
leftWall = box(pos=vector(-roomWidth/2, 0, 0), size=vector(wallThickness, roomHeight, roomDepth), color=color.white)
rightWall = box(pos=vector(roomWidth/2, 0, 0), size=vector(wallThickness, roomHeight, roomDepth), color=color.white)
backWall = box(pos=vector(0, 0, -roomDepth/2), size=vector(roomWidth, roomHeight, wallThickness), color=color.white)

marble = sphere(radius=mRadius, color=color.red)

deltaX = uniform(0, mMaxVelocity)
deltaY = uniform(0, mMaxVelocity)
deltaZ = uniform(0, mMaxVelocity)

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
    rate(speedMultiplicator * baseSpeed)

    effectiveRadius = mRadius * marbleScale
    marble.radius = effectiveRadius
    marble.color = marbleColor
    marble.opacity = marbleOpacity

    if not isRunning:
        continue

    xPos = xPos + deltaX
    yPos = yPos + deltaY
    zPos = zPos + deltaZ

    # Left and right wall collisions
    if xPos - effectiveRadius < leftBoundary:
        xPos = leftBoundary + effectiveRadius
        deltaX = deltaX * -1
    elif xPos + effectiveRadius > rightBoundary:
        xPos = rightBoundary - effectiveRadius
        deltaX = deltaX * -1

    # Floor and ceiling colisions
    if yPos - effectiveRadius < bottomBoundary:
        yPos = bottomBoundary + effectiveRadius
        deltaY = deltaY * -1
    elif yPos + effectiveRadius > topBoundary:
        yPos = topBoundary - effectiveRadius
        deltaY = deltaY * -1

    # Back and front wall colisions
    if zPos - effectiveRadius < backBoundary:
        zPos = backBoundary + effectiveRadius
        deltaZ = deltaZ * -1
    elif zPos + effectiveRadius > frontBoundary:
        zPos = frontBoundary - effectiveRadius
        deltaZ = deltaZ * -1

    marble.pos = vector(xPos, yPos, zPos)
