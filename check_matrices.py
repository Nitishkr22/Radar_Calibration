import numpy as np
import math

ay = math.radians(98)
az = math.radians(-87.6)
ax = math.radians(100)


Ry = np.array([[np.cos(ay), 0, np.sin(ay)],[0, 1, 0],[-np.sin(ay), 0, np.cos(ay)]]) #about y axis
Rz = np.array([[np.cos(az), -np.sin(az), 0], [np.sin(az), np.cos(az), 0], [0, 0, 1]]) #about z axis
Rx = np.array([[1, 0, 0], [0, np.cos(ax), -np.sin(ax)], [0, np.sin(ax), np.cos(ax)]]) #about x axis
rot_mat21 =np.dot(Ry,Rz) 

# print("rotation_Matrix: ", rot_mat21)

Intrensic = np.array([[1462.4625, 0, 968.4078],
                       [0, 1464.2939, 603.0266],
                       [0, 0, 1]])

print("Intrensic_matrix: ",Intrensic)