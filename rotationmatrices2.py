# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:28:51 2020

@author: hung
"""

import numpy as np

a1 = 1 #length of link a1 in cm
a2 = 1 #length of link a2 in cm
a3 = 1 #length of link a3 in cm
a4 = 1 #length of link a4 in cm

Tx = 10 #Xtheta angle in degrees
Ty = 70 #Ytheta angle in degrees
Tz = 70 #Ztheta angle in degrees


Tx = (Tx/180.0)*np.pi #theta x in radians
Ty = (Ty/180.0)*np.pi #theta y in radians
Tz = (Tz/180.0)*np.pi #theta z in radians


R0_1 = [ [np.cos(Tx),-np.sin(Tx), 0], [np.sin(Tx), np.cos(Tx), 0], [0, 0, 1] ]
R1_2 = [ [np.cos(Ty),-np.sin(Ty), 0], [np.sin(Ty), np.cos(Ty), 0], [0, 0, 1] ]

R0_2 = np.dot(R0_1, R1_2)

#print(R0_2)

d0_1 = [[a2*np.cos(Tx)], [a2*np.sin(Tx)], [a1]]
d1_2 = [[a4*np.cos(Ty)], [a4*np.sin(Ty)], [a3]]

print(np.matrix(d0_1))
print(np.matrix(d1_2))

#R1_2 = [ [1, 0, 0],[0, np.cos(T2),-np.sin(T2)], [0, np.sin(T2), np.cos(T2)] ]


"""
Xr = [[1, 0, 0, 0],[0, np.cos(Tx),-np.sin(Tx), 0], [0, np.sin(Tx), np.cos(Tx), 0], [0, 0, 0, 1]]

Yr = [[np.cos(Ty), 0, np.sin(Ty), 0], [0, 1, 0, 0], [-np.sin(Ty), 0, np.cos(Ty), 0], [0, 0, 0, 1]]

Zr = [[np.cos(Tz),-np.sin(Tz), 0, 0], [np.sin(Tz), np.cos(Tz), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

point = [[100], [70], [50],[1]]

new1 = np.dot(Xr, Zr)
new2 = np.dot(new1, point)

#print(new1)

d0_1 = [[a2*np.cos(Tx)], [a2*np.sin(Tx)], [a1]]
d1_2 = [[a4*np.cos(Tz)], [a4*np.sin(Tz)], [a3]]

print(np.matrix(d0_1))
print(np.matrix(d1_2))
"""







