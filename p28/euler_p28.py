import numpy
def solveit():
  summer = 1
  current = 1
  for i in numpy.arange(2,1002,2):
    for j in range(4):
      current += i
      summer += current
  print summer
