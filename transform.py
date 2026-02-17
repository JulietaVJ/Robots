import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

from sympy import Symbol, Matrix

#Matriz R

#theta = Symbol('theta')
#R = Matrix(rot2(theta))
#print(R)

#Convertir grados a radianes

theta_deg = 30
theta_rad = np.deg2rad(theta_deg)

#R = rot2(theta_rad)
#print(R)


#Matriz de traslación Rotación
#R2 = trot2(theta_rad)
#print(R2)

#Rotación y traslación A
T0 = transl2(0,0) #Referencia
trplot2(T0, frame="0", color="k")

TA = transl2(1, 2) @ trot2(30, 'deg') #Transformación A
print(TA)
trplot2(TA, frame="A", color="b")

#Punto P
P = np.array([4,3]) 
plot_point(P, 'ko', text='P') 
print(P)

P1 = homtrans(np.linalg.inv(TA), P)
print(P1)

#Rotación y traslación B
TB = trot2(30, 'deg') @ transl2(1, 2) #Transformación B
print(TB)
trplot2(TB, frame="B", color="r")

#trplot2(R) #Dibujamos en plot
plt.axis('equal')
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Transformación 2D')
plt.show() #Mostrar ventana de plot


