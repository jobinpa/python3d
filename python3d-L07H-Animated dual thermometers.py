import math
from vpython import *
import numpy as np

scene = canvas()
scene.height = 500
scene.width = 250
scene.range = scene.width / 2

minTemperature = 0
maxTemperature = 100

t1Temp = minTemperature
t1Step = (maxTemperature - minTemperature) / 1000.0

t2Temp = minTemperature
t2Step = t1Step * 2


def updateTemp(temp, step):
    temp = temp + step
    if temp < minTemperature or temp > maxTemperature:
        step = step * -1
    return (temp, step)


class Thermometer:
    def __init__(self, width, height, pos, minTemp, maxTemp, tickStep):
        if width <= 0:
            raise ValueError('Width must be greater than 0')
        if height <= 0:
            raise ValueError('Height must be greater than 0')
        if maxTemp <= minTemp:
            raise ValueError('Max temp must be greater than min temp.')

        self.__width__ = width
        self.__height__ = height
        self.__pos__ = pos
        self.__minTemp__ = minTemp
        self.__maxTemp__ = maxTemp
        self.__tickStep__ = tickStep
        self.__currentTemp__ = minTemp

        self.__ticks__ = []

        self.__sphere__ = sphere(color=color.white, opacity=0.25)

        self.__tube__ = cylinder(color=color.white, opacity=0.25)
        self.__tube__.rotate(angle=radians(90), axis=vector(0, 0, 1))

        self.__mercuryBlob__ = sphere(color=color.red)

        self.__mercuryColumn__ = cylinder(color=color.red)
        self.__mercuryColumn__.rotate(angle=radians(90), axis=vector(0, 0, 1))

        self.__ticks__ = []
        if self.__tickStep__ > 0:
            stepCount = math.ceil((self.__maxTemp__ - self.__minTemp__) / self.__tickStep__)
            # +1 because we also want a tick at the lowest level
            for i in range(0, stepCount + 1):
                r = ring(thickness=1, opacity=0.25, color=color.black)
                r.rotate(angle=radians(90), axis=vector(0, 0, 1))
                self.__ticks__.append(r)

        self.__updateDimensionsAndPositions__()
        self.__setMercuryLevel__()

    def __updateDimensionsAndPositions__(self):
        self.__sphere__.radius = self.__width__ / 2
        self.__sphere__.pos = vector(
            self.__pos__.x,
            self.__pos__.y - (self.__height__ / 2) + self.__sphere__.radius,
            self.__pos__.z)

        self.__tube__.radius = self.__sphere__.radius * 0.35
        self.__tube__.length = self.__height__ - self.__sphere__.radius
        self.__tube__.pos = self.__sphere__.pos

        self.__mercuryBlob__.radius = self.__sphere__.radius * .85
        self.__mercuryBlob__.pos = self.__sphere__.pos

        self.__mercuryColumn__.radius = self.__tube__.radius * 0.5
        self.__mercuryColumn__.length = self.__sphere__.radius
        self.__mercuryColumn__.pos = self.__sphere__.pos

        if len(self.__ticks__) > 0:
            # -1 as we don't want to count the tick for the lowest level
            stepHeight = (self.__tube__.length - self.__sphere__.radius) / (len(self.__ticks__) - 1)
            for i in range(0, len(self.__ticks__)):
                t = self.__ticks__[i]
                t.radius = self.__tube__.radius
                t.pos = vector(
                    self.__sphere__.pos.x,
                    self.__sphere__.pos.y + self.__sphere__.radius + i * stepHeight,
                    self.__sphere__.pos.z)

    def __setMercuryLevel__(self):
        tempRange = self.__maxTemp__ - self.__minTemp__
        mercuryRange = self.__tube__.length - self.__sphere__.radius
        tempDelta = self.__currentTemp__ - self.__minTemp__
        mercuryDelta = tempDelta * mercuryRange / tempRange
        self.__mercuryColumn__.length = self.__sphere__.radius + mercuryDelta

    def setTemperature(self, temp):
        if temp < self.__minTemp__:
            print(f'***WARNING*** Trying to set temperature to unsafe low value {temp}.')
            temp = self.__minTemp__
        if temp > self.__maxTemp__:
            print(f'***WARNING*** Trying to set temperature to unsafe high value {temp}.')
            temp = self.__maxTemp__
        self.__currentTemp__ = temp
        self.__setMercuryLevel__()


t1 = Thermometer(width=100, height=360, pos=vector(-50, 0, 0), minTemp=minTemperature, maxTemp=maxTemperature, tickStep=5)
t2 = Thermometer(width=100, height=360, pos=vector(50, 0, 0), minTemp=minTemperature, maxTemp=maxTemperature, tickStep=5)

while True:
    rate(250)
    t1Temp, t1Step = updateTemp(t1Temp, t1Step)
    t1.setTemperature(minTemperature if t1Temp < minTemperature else maxTemperature if t1Temp > maxTemperature else t1Temp)
    t2Temp, t2Step = updateTemp(t2Temp, t2Step)
    t2.setTemperature(minTemperature if t2Temp < minTemperature else maxTemperature if t2Temp > maxTemperature else t2Temp)
