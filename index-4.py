from triangle.plot import plot
from numpy import *
import matplotlib.pyplot as plt

theta = linspace(0, 2*pi, 33)[:-1]
pts = vstack((cos(theta), sin(theta))).T
plot(plt, pts)
plt.show()