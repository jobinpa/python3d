from vpython import *
from time import *

#red marble

floor = box( pos=vector(0, -5, 0), color=color.white, length=10, height=0.1, width=10)
leftWall = box( pos=vector(-5, 0, 0), color=color.white, length=0.1, height=10, width=10)
ceiling = box( pos=vector(0, 5, 0), color=color.white, length=10, height=0.1, width=10)
rightWall = box( pos=vector(5, 0, 0), color=color.white, length=0.1, height=10, width=10)
backWall = box( pos=vector(0, 0, -5), color=color.white, length=10, height=10, width=0.1)

marble = sphere(radius=0.5, color=color.red)

while True:
    pass