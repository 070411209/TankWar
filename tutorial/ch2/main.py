#!/usr/local/bin/python
# -*- coding: gbk -*-

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from numpy import angle, linspace
import numpy as np

#3D Plotting
fig = plt.figure()
ax = plt.axes(projection="3d")

# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
# z = np.linspace(-2, 2, 100)
# r = z**2 + 1
# x = r * np.sin(theta)
# y = r * np.cos(theta)
# ax.plot(x, y, z, label='parametric curve')
# ax.legend()

# angle = linspace(0,2*np.pi*5, 100)
# x = np.cos(angle)
# y = np.sin(angle)
# z = linspace(0,5, 100)

# ax.plot3D(x,y,z)


 
# X = np.arange(-2, 2, 0.1)
# Y = np.arange(-2, 2, 0.1)
# X, Y = np.meshgrid(X, Y)
# Z = np.sqrt(X ** 2 + Y ** 2)
 
# ax.plot_surface(X, Y, Z, cmap=plt.cm.winter)

# x = np.arange(-5, 5, 0.1)
# y = np.arange(-5, 5, 0.1)
# x,y = np.meshgrid(x, y)
# R = np.sqrt(x**2+y**2)
# z = np.sin(R)

# ax.plot_surface(x, y, z)

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X,Y = np.meshgrid(x,y)
Z1 = np.exp(-(X+1)**2-(Y+0.5)**2)
Z2 = np.exp(-(X-1)**2-(Y-0.5)**2)

Z=(Z1-Z2)*2

CS=ax.plot_surface(X,Y,Z, camp=plt.cm.coolwarm)
# ax.plot_surface(X, Y, Z, cmap=plt.cm.winter)
#Labeling
ax.set_xlabel('X Axes')
ax.set_ylabel('Y Axes')
ax.set_zlabel('Z Axes')

plt.show()
