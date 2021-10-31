from vpython import *
import numpy as np
import math

scene = canvas()
scene.height = 500
scene.width = 200
scene.range = scene.width / 2

minTemperature = 0
maxTemperature = 100

width = 100
height = 360
pos = vector(0, 0, 0)
minTemp = 0
maxTemp = 100
tickStep = 5

glassSphere = sphere(color=color.white, opacity=0.25)
glassSphere.radius = width / 2
glassSphere.pos = vector(
    pos.x,
    pos.y - (height / 2) + glassSphere.radius,
    pos.z)

tube = cylinder(color=color.white, opacity=0.25)
tube.rotate(angle=radians(90), axis=vector(0, 0, 1))
tube.radius = glassSphere.radius * 0.35
tube.length = height - glassSphere.radius
tube.pos = glassSphere.pos

mercuryBlob = sphere(color=color.red)
mercuryBlob.radius = glassSphere.radius * .85
mercuryBlob.pos = glassSphere.pos

mercuryColumn = cylinder(color=color.red)
mercuryColumn.rotate(angle=radians(90), axis=vector(0, 0, 1))
mercuryColumn.radius = tube.radius * 0.5
mercuryColumn.length = glassSphere.radius
mercuryColumn.pos = glassSphere.pos

if (tickStep > 0):
    stepCount = math.ceil((maxTemp - minTemp) / tickStep)
    stepHeight = (tube.length - glassSphere.radius) / stepCount

    # +1 because we also want a tick at the lowest level
    for i in range(0, stepCount + 1):
        r = ring(thickness=1, opacity=0.25, color=color.black)
        r.rotate(angle=radians(90), axis=vector(0, 0, 1))
        r.radius = tube.radius
        r.pos = vector(
            glassSphere.pos.x,
            glassSphere.pos.y + glassSphere.radius + i * stepHeight,
            glassSphere.pos.z)

mercuryColumnLowestLevel = glassSphere.radius
mercuryColumnHighestLevel = tube.length

while True:
    for l in np.linspace(mercuryColumnLowestLevel, mercuryColumnHighestLevel, 1000):
        rate(250)
        mercuryColumn.length = l

    for l in np.linspace(mercuryColumnHighestLevel, mercuryColumnLowestLevel, 1000):
        rate(250)
        mercuryColumn.length = l
