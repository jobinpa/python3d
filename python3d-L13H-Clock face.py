import numpy as np
from vpython import *


class WallClock:
    def __init__(self):
        self.clockPosition = vector(0, 0, 0)
        self.clockRadius = 1.0
        self.clockThickness = 0.1
        self.clockColor = color.white

        self.ticksDistanceFromCenter = self.clockRadius * 0.9

        self.minorTicksRadius = self.clockRadius / 100
        self.minorTicksColor = color.black

        self.majorTicksRadius = self.minorTicksRadius * 5
        self.majorTicksColor = color.black

        self.__addFrame__()
        self.__addMinorTicks__()
        self.__addMajorTicks__()

    def __addFrame__(self):
        cylinder(
            radius=self.clockRadius,
            length=self.clockThickness,
            axis=vector(0, 0, 1),
            pos=self.clockPosition,
            color=self.clockColor,
            emissive=True)

    def __addMinorTicks__(self):
        for d in np.linspace(0, 360, 60, endpoint=False):
            theta = np.radians(d)
            tickX = (self.ticksDistanceFromCenter * np.cos(theta)) + self.clockPosition.x
            tickY = (self.ticksDistanceFromCenter * np.sin(theta)) + self.clockPosition.y
            tickZ = self.clockPosition.z + self.clockThickness
            cylinder(
                radius=self.minorTicksRadius,
                length=0.001,
                axis=vector(0, 0, 1),
                pos=vector(tickX, tickY, tickZ),
                color=self.minorTicksColor,
                emissive=True)

    def __addMajorTicks__(self):
        for d in np.linspace(0, 360, 12, endpoint=False):
            theta = np.radians(d)
            tickX = (self.ticksDistanceFromCenter * np.cos(theta)) + self.clockPosition.x
            tickY = (self.ticksDistanceFromCenter * np.sin(theta)) + self.clockPosition.y
            tickZ = self.clockPosition.z + self.clockThickness
            cylinder(
                radius=self.majorTicksRadius,
                length=0.001,
                axis=vector(0, 0, 1),
                pos=vector(tickX, tickY, tickZ),
                color=self.majorTicksColor,
                emissive=True)


clock = WallClock()

while True:
    rate(1)
    pass
