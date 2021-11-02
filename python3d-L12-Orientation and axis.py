from vpython import *
import numpy as np

arrowL = 2
arrowT = 0.02

xArrow = arrow(axis=vector(1, 0, 0), color=color.red, length=arrowL, shaftwidth = arrowT)
yArrow = arrow(axis=vector(0, 1, 0), color=color.green, length=arrowL, shaftwidth = arrowT)
zArrow = arrow(axis=vector(0, 0, 1), color=color.blue, length=arrowL, shaftwidth = arrowT)

# WARNING: Changing arrow axis after creation resets the arrow length

# Create an arrow at 45 degrees.
# 90 degrees = pi/2, 180 degrees = pi, 270 degrees = 3pi/2, 360 degrees = 2pi
# Theta is expressed as radians
# Formula to convert degrees into radians: 2pi(degrees/360)

degrees = 0
theta = (2 * np.pi) * (degrees/360)
arrowX = arrowL * np.cos(theta)
arrowY = arrowL * np.sin(theta)
pntArrow = arrow(
    axis=vector(arrowX, arrowY, 0), 
    color=color.orange, 
    length=arrowL, 
    shaftwidth=arrowT)

while True:
    rate(10)
    degrees = degrees + 1
    if degrees > 360:
        degrees = 0 + (degrees - 360)

    theta = (2 * np.pi) * (degrees/360)
    arrowX = arrowL * np.cos(theta)
    arrowY = arrowL * np.sin(theta)

    pntArrow.axis = vector(arrowX, arrowY, 0)
    pntArrow.length = arrowL

    pass