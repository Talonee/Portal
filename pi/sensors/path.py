import matplotlib.path as mplPath
import matplotlib.pyplot as plt
import numpy as np
from random import randint
import os

#mode is whether it is inclusion or exclusion
#true - inclusion, false exclusion

class Path:
    def __init__(self, points = None, mode = True):
        self.mode = mode
        self.path = None
        
        if points != None:
            self.setPoints(points)
        
    def setPoints(self, points, save = False):
        self.path_points = points
        self.setPointComponents()
        self.createPath()
        
        if save:
            self.savePath()
        
    def setPointComponents(self):
        self.path_x = []
        self.path_y = []

        for point in self.path_points:
            self.path_x.append(point[0])
            self.path_y.append(point[1])

        self.path_x.append(self.path_points[0][0])
        self.path_y.append(self.path_points[0][1])
     
    def createPath(self):
        self.path = mplPath.Path(np.array(self.path_points))
        
    def savePath(self, fp = 'path.txt'):
        if os.path.exists(fp):
            os.remove(fp)
        np.savetxt(fp, np.array(self.path_points))

    def loadPath(self, fp = 'path.txt'):
        self.setPoints(np.loadtxt(fp))
    
    def showPath(self,xmin = 0, xmax = 10, ymin = 0, ymax = 10, color = None, points = None):
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        plt.grid()
        
        if color == None:
            color = 'blue' if self.mode else 'red'

        plt.plot(self.path_x, self.path_y, color = color)
        
        if points:
            for point in points:
                point_color = 'green' if self.checkPoint(point) else 'red'
                plt.plot([point[0]], [point[1]], marker="o", linewidth=0, color=point_color)
        plt.show()

    def checkPoint(self, point, valid = True):
        p_in_p = self.path.contains_point(point) #point in path
        result = p_in_p if not valid else not(bool(p_in_p^self.mode))
        return result
    
if __name__ == '__main__':
    inclusion = Path()
    inclusion.setPoints([[0,2],[1, 7], [3, 9], [8,5], [5, 3], [1,1]])
    inclusion.showPath()
    
    exclusion = Path(points = [[2,4],[2, 6], [4, 6], [6,4]], mode = False)
    exclusion.showPath()
    
    test_points = []
    for i in range(10):
      test_points.append([randint(0,10), randint(0,10)])
      
    print("Inclusion Point Test: [5,5]",  inclusion.checkPoint([5,5]))
    print("Inclusion Point Test: [9,5]", inclusion.checkPoint([9,5]))
    
    print("Exclusion Point Test: [5,5]",  exclusion.checkPoint([4,5], False))
    print("Exclusion Point Test: [9,5]", exclusion.checkPoint([9,5], False))
    
    print("Exclusion Valid Point Test: [5,5]",  exclusion.checkPoint([4,5]))
    print("Exclusion Valid Point Test: [9,5]", exclusion.checkPoint([9,5]))
    
    inclusion.showPath(color = 'purple', points = test_points)
    

'''   
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.grid()

    plt.plot(path_x, path_y)
    plt.plot(exclusion_x, exclusion_y, linestyle='dashed', color='red')

    for point in test_points:

      if poly_path.contains_point(point):
        point_color = 'green'
      else:
        point_color = 'red'
      if exclu_path.contains_point(point):
        point_color = 'red'

      plt.plot([point[0]], [point[1]], marker="o", linewidth=0, color=point_color)

    plt.show()
'''