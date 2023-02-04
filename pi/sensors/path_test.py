import matplotlib.path as mplPath
import matplotlib.pyplot as plt
import numpy as np
from random import uniform
import time
from map_draw import *

sizex = 500
sizey = 500
tol = .1 #10% tolerance

path_points = get_map_pygame(sizex,sizey)

path_x = []
path_y = []

for point in path_points:
  path_x.append(point[0])
  path_y.append(point[1])

path_x.append(path_points[0][0])
path_y.append(path_points[0][1])

plt.xlim(0, sizex)
plt.ylim(0, sizey)
plt.grid()

plt.plot(path_x, path_y)
plt.show()
poly_path = mplPath.Path(np.array(path_points))

test_points = []
times = 0
points = 100

for i in range(points):
    refTime = time.time()
    point = [uniform(0,sizex), uniform(0,sizey)]
    test_points.append(point)
    poly_path.contains_point(point, radius=int(sizex*tol))
    times+=time.time()-refTime
    #print(point, "is in polygon:", poly_path.contains_point(point))

print("Average Time:",times/points*1000,"ms")
  
plt.xlim(0, sizex)
plt.ylim(0, sizey)
plt.grid()

plt.plot(path_x, path_y)

for point in test_points:
  if poly_path.contains_point(point):
    point_color = 'green'
  else:
    point_color = 'red'

  plt.plot([point[0]], [point[1]], marker="o", linewidth=0, color=point_color)

plt.show()
