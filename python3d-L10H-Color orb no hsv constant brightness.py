import numpy as np
from vpython import *


def incrementChannel(chan, step):
    chan = chan + step
    if chan < 0 or chan > 1.5:
        step = step * -1
    return (chan, step)


# We get the constant brightness by aligning the rgb channels so at any
# given point of time the sum of all the channel is always around 2.
# See https://youtu.be/dfhTeqxfj1o for more details.
rChannel = 1
bChannel = 1
gChannel = 0

orb = sphere(radius=0.99, color=vector(rChannel, gChannel, bChannel), texture=textures.metal, emissive=True)

rChannelStep = 0.003
bChannelStep = -0.003
gChannelStep = 0.003

rotation = radians(360/1000)
while True:
    rate(60)
    rChannel, rChannelStep = incrementChannel(rChannel, rChannelStep)
    gChannel, gChannelStep = incrementChannel(gChannel, gChannelStep)
    bChannel, bChannelStep = incrementChannel(bChannel, bChannelStep)

    orb.color = vector(
        1 if rChannel > 1 else 0 if rChannel < 0 else rChannel,
        1 if gChannel > 1 else 0 if gChannel < 0 else gChannel,
        1 if bChannel > 1 else 0 if bChannel < 0 else bChannel)

    scene.forward = rotate(scene.forward, angle=rotation, axis=vector(0, 1, 0))
    print(orb.color, orb.color.x + orb.color.y + orb.color.z)
