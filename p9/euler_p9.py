import numpy

def solveit():
  for i in range(1,500):
    for j in range(1,500):
      k = numpy.sqrt(i*i + j*j)
      if i + j + k == 1000:
        print i*j*k
        return True
