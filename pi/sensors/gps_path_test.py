import numpy as np
from random import uniform
import time, os
from map_draw import *
from gps import GPS
from path import Path

redo = False
gps = GPS()

sizex = 85 #85 for avg yard
sizey = 85
tol = .1 #10% tolerance


if os.path.exists('lawn.txt'):
    lawn = Path()
    lawn.loadPath('lawn.txt')
else:
    lawn = Path(points = get_map_pygame(sizex,sizey))
    lawn.savePath('lawn.txt')

lawn.showPath(xmax = sizex, ymax = sizey)
print('Setting The Origin')
gps.setRel()


test_points = []
times = 0
points = 10

for i in range(points):
    refTime = time.time()
    point = gps.getRelXY(complete = True, display = False)
    point[0] += uniform(0,sizex)
    point[1] += uniform(0,sizey)
    test_points.append(point)
    times+=time.time()-refTime
    #print(point)

print("Average Time:",times/points*1000,"ms")
  
lawn.showPath(xmax = sizex, ymax = sizey, points = test_points)
