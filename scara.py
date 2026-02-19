import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

from sympy import Symbol, Matrix

T0 = transl2(0,0) #Referencia
trplot2(T0, frame="0", color="k")

TA = trot2(55, 'deg') 
trplot2(TA, frame="A", color="b")
plot_circle(4, (0,0), 'b--')

TBA = TA @ transl2(4, 0) @ trot2(72, 'deg')
trplot2(TBA, frame="B", color="g")
origin_TBA = TBA[:2, 2]
plot_circle(3, (origin_TBA[0], origin_TBA[1]), 'g--')

TCBA = TBA @ transl2(3, 0) 
trplot2(TCBA, frame="C", color="r")
print(TCBA)

origin_TCBA = TCBA[:2, 2]
P = np.array([origin_TCBA[0], origin_TCBA[1]])
plot_point(P, 'ro', text='P')
print('Coordenadas en T0: {:.4f}, {:.4f}'.format(P[0], P[1]))



plt.axis('equal')
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Transformación 2D')
plt.show() #Mostrar ventana de plot