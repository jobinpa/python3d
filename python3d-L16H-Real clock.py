import datetime
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

        self.hourArm = None
        self.hourArmLength = self.ticksDistanceFromCenter * 0.70
        self.hourArmWidth = self.ticksDistanceFromCenter * 0.08
        self.hourArmColor = color.green

        self.minuteArm = None
        self.minuteArmLength = self.ticksDistanceFromCenter * 0.90
        self.minuteArmWidth = self.ticksDistanceFromCenter * 0.08
        self.minuteArmColor = color.blue

        self.secondArm = None
        self.secondArmLength = self.ticksDistanceFromCenter * 0.85
        self.secondArmWidth = self.ticksDistanceFromCenter * 0.02
        self.secondArmColor = color.red

        self.centralShaftRadius = max(
            self.hourArmWidth,
            self.minuteArmWidth,
            self.secondArmWidth) * 0.6
        self.centralShaftColor = color.black

        # The hour arm is the baseline. His revolution is based on a 12h period.
        # We calculate the movement of the hour arm per clock unit (second). The
        # movement is expressed in radians (2*pi equals 360 degrees). The minute
        # and second arm speeds are relative to the hour arm:
        #  - The minute arm is 12x faster than the hour arm
        #  - The second arm is 60x faster than the minute arm
        self.__SECONDS_IN_FULL_HOUR_ARM_REVOLUTION__ = 12 * 60 * 60
        self.__HOUR_ARM_RADIANS_PER_SECOND__ = (2 * np.pi) / self.__SECONDS_IN_FULL_HOUR_ARM_REVOLUTION__
        self.__MINUTE_ARM_RADIANS_PER_SECOND__ = 12 * self.__HOUR_ARM_RADIANS_PER_SECOND__
        self.__SECOND_ARM_RADIANS_PER_SECOND__ = 60 * self.__MINUTE_ARM_RADIANS_PER_SECOND__

        self.__addFrame__()
        self.__addMinorTicks__()
        self.__addMajorTicks__()
        self.__addHourArm__()
        self.__addMinuteArm__()
        self.__addSecondArm__()
        self.__addCentralShaft__()

        self.setTime(0, 0, 0)

    def setTime(self, hours, minutes, seconds):
        R360D = 2*np.pi  # 360 degrees expressed in radians
        R90D = np.pi/2  # 90 degrees expressed in radians

        totalSeconds = seconds + (minutes * 60) + (hours * 60 * 60)

        # The clock 0 is at 12h, which is 90 degrees
        # We need to shift our angles by -90 degrees

        hourArmRadians = R360D - ((self.__HOUR_ARM_RADIANS_PER_SECOND__ * totalSeconds - R90D) % R360D)
        self.hourArm.axis = vector(
            self.hourArmLength * np.cos(hourArmRadians),
            self.hourArmLength * np.sin(hourArmRadians),
            0)
        self.hourArm.length = self.hourArmLength

        minuteArmRadians = R360D - ((self.__MINUTE_ARM_RADIANS_PER_SECOND__ * totalSeconds - R90D) % R360D)
        self.minuteArm.axis = vector(
            self.minuteArmLength * np.cos(minuteArmRadians),
            self.minuteArmLength * np.sin(minuteArmRadians),
            0)
        self.minuteArm.length = self.minuteArmLength

        secondArmRadians = R360D - ((self.__SECOND_ARM_RADIANS_PER_SECOND__ * totalSeconds - R90D) % R360D)
        self.secondArm.axis = vector(
            self.secondArmLength * np.cos(secondArmRadians),
            self.secondArmLength * np.sin(secondArmRadians),
            0)
        self.secondArm.length = self.secondArmLength

    def __addFrame__(self):
        cylinder(
            radius=self.clockRadius,
            length=self.clockThickness,
            axis=vector(0, 0, 1),
            pos=self.clockPosition,
            color=self.clockColor)

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

    def __addHourArm__(self):
        self.hourArm = arrow(
            axis=vector(1, 0, 0),
            color=self.hourArmColor,
            length=self.hourArmLength * 0.9,
            shaftwidth=self.hourArmWidth,
            headwidth=self.hourArmWidth,
            headlength=self.hourArmLength * 0.1,
            pos=vector(
                self.clockPosition.x,
                self.clockPosition.y,
                self.clockPosition.z + self.clockThickness + self.hourArmWidth / 2))

    def __addMinuteArm__(self):
        self.minuteArm = arrow(
            axis=vector(1, 0, 0),
            color=self.minuteArmColor,
            length=self.minuteArmLength * 0.9,
            shaftwidth=self.minuteArmWidth,
            headwidth=self.minuteArmWidth,
            headlength=self.minuteArmLength * 0.1,
            pos=vector(
                self.hourArm.pos.x,
                self.hourArm.pos.y,
                self.hourArm.pos.z + (self.hourArmWidth / 2) + (self.minuteArmWidth / 2)))

    def __addSecondArm__(self):
        self.secondArm = arrow(
            axis=vector(1, 0, 0),
            color=self.secondArmColor,
            length=self.secondArmLength * 0.9,
            shaftwidth=self.secondArmWidth,
            headwidth=0.001,
            headlength=0.001,
            pos=vector(
                self.minuteArm.pos.x,
                self.minuteArm.pos.y,
                self.minuteArm.pos.z + (self.minuteArmWidth / 2) + (self.secondArmWidth / 2)))

    def __addCentralShaft__(self):
        cylinder(
            radius=self.centralShaftRadius,
            length=self.hourArmWidth + self.minuteArmWidth + self.secondArmWidth + 0.01,
            axis=vector(0, 0, 1),
            pos=vector(self.clockPosition.x, self.clockPosition.y, self.clockPosition.z + self.clockThickness),
            color=self.centralShaftColor)


clock = WallClock()

while True:
    now = datetime.datetime.now()
    clock.setTime(now.hour, now.minute, now.second)
    rate(10)
