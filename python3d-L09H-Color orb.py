import colorsys
import numpy as np
from vpython import *

orb = sphere(radius=0.99, color=color.white, texture=textures.metal, emissive=True)

sampleCount = 1000
while True:
    for h in np.linspace(0, 360, sampleCount, endpoint=False):
        rate(60)
        rgb = colorsys.hsv_to_rgb(h/360, 1.0, 1.0)
        orb.color = vector(rgb[0], rgb[1], rgb[2])
        scene.forward = rotate(scene.forward, angle=radians(360/sampleCount), axis=vector(0, 1, 0))
        print(orb.color, orb.color.x + orb.color.y + orb.color.z)