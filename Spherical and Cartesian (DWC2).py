import math
import n

import numpy as np
def rnd(x,n):
    res = float(str(round(x,n)))
    return res

def spherical_to_cartesian(r, theta, phi):
    x = round(r * np.cos(phi) * np.cos(theta),5)
    y = round(r * np.sin(phi) * np.cos(theta),5)
    z = round(r * np.sin(theta),5)

    return x, y, z

def cartesian_to_spherical(x, y, z):
    r = round(((x**2)+(y**2)+(z**2))*0.5,5)
    try:
        phi = round(np.arctan(x**2+y**2)**0.5/z,5)
    except:
        phi = np.pi/2
    try:
        theta = round(np.arctan(y/x)
    except:
        theta = np.pi/2
    return rnd(r,5), rnd(theta,5), rnd(phi,5)

r = float(input("What is your radius? \n"))
theta = float(input("What is your theta? \n"))
phi = float(input("What is your phi? \n"))
output = spherical_to_cartesian(r, theta, phi)
print(output)

