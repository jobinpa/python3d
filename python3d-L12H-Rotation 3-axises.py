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
    shaftwidth=arrowT * 2)

delay = 20
while True:
    # (x,y) rotation
    for d in np.linspace(0, 360, 360):
        rate(delay)
        theta = np.radians(d)
        arrowX = arrowL * np.cos(theta)
        arrowY = arrowL * np.sin(theta)
        pntArrow.axis = vector(arrowX, arrowY, 0)
        pntArrow.length = arrowL

    # (x, z) rotation
    for d in np.linspace(0, 360, 360):
        rate(delay)
        theta = np.radians(d)
        arrowX = arrowL * np.cos(theta)
        arrowZ = arrowL * np.sin(theta)
        pntArrow.axis = vector(arrowX, 0, arrowZ)
        pntArrow.length = arrowL

    # (x, y) partial rotation to bring arrow to z
    for d in np.linspace(0, 90, 90):
        rate(delay)
        theta = np.radians(d)
        arrowX = arrowL * np.cos(theta)
        arrowZ = arrowL * np.sin(theta)
        pntArrow.axis = vector(arrowX, 0, arrowZ)
        pntArrow.length = arrowL

    # (y, z) rotation
    for d in np.linspace(0, 360, 360):
        rate(delay)
        theta = np.radians(d)
        arrowZ = arrowL * np.cos(theta)
        arrowY = arrowL * np.sin(theta)
        pntArrow.axis = vector(0, arrowY, arrowZ)
        pntArrow.length = arrowL

    # (x, y) partial rotation to bring arrow to x
    for d in np.linspace(90, 360, 270):
        rate(delay)
        theta = np.radians(d)
        arrowX = arrowL * np.cos(theta)
        arrowZ = arrowL * np.sin(theta)
        pntArrow.axis = vector(arrowX, 0, arrowZ)
        pntArrow.length = arrowL