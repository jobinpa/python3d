from vpython import *
import numpy as np

mySphere = sphere(radius=1, color=color.red, opacity=0.5)

while True:
    for myRadius in np.linspace(0.1, 1, 1000):
        rate(250)
        mySphere.radius = myRadius
    
    for myRadius in np.linspace(1, 0.1, 1000):
        rate(250)
        mySphere.radius = myRadius

    pass