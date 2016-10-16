from math import exp

n = "n"
mean = "mean"
points = {"bing":{mean:0, n:0},
          "yahoo":{mean:0, n:0},
          "google":{mean:0, n:0}}

def addPoints(engine, positionInSearch):
    if(positionInSearch > 0 and positionInSearch <= 10):
        points[engine][mean] = (points[engine][mean]*points[engine][n] + 1/pow(1.15, positionInSearch-1))/(points[engine][n] + 1)
    points[engine][n] = points[engine][n] + 1

def getPoints(engine):
    return points[engine][mean]