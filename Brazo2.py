import numpy as np
import matplotlib.pyplot as plt 
from spatialmath import * 
from spatialmath.base import *
from math import pi

np.set_printoptions(
    formatter={'float': lambda x: f"{x:8.4g}" if abs(x) < 1e-10 else f"{x:8.4g}"})

# Referencia TO
T0 = rotz(0, unit="deg")
trplot (T0, dims=[-1, 1, -1, 1, -1, 1], color='k') #Dibujar
# Sistema de coordenadas rotado (TA)
TA = rotz (90, unit='deg')
trplot (TA, dims=[-1, 1, -1, 1, -1, 1], color='g') #Dibujar
# Definir el punto P con respecto a TO
P = np. array([1, 1, 0])
ax = plt.gca()
ax. scatter (P[0], P[1], P[2], color='r', label="p")
# Configurar plot
plt.gca(). view_init(elev=25, azim=44)

print("P en TO: ", P)
Pos_TA = P @ TA
print("Posmult. de P respecto a TA: ", Pos_TA)
#Perspectiva

# Mostrar la trama
plt.show()