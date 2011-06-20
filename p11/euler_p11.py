import numpy
def solveit():
  grid = numpy.zeros((20,20), dtype = numpy.uint64)
  ins = open("in.txt","r")
  j = 0
  for line in ins:
    if len(line) > 1:
      line = line.split(" ")
      for i in range(20):
        grid[j][i] = int(line[i])
    j += 1
  s = 0
  ans = []
  for row in range(20):
    for col in range(20):
      for walk1 in [-3,0,3]:
        for walk2 in [-3,0,3]:
          if walk1 != 0 or walk2 != 0:
            if row + walk1 >= 0 and row + walk1 < 20:
              if col + walk2 >= 0 and col + walk2 < 20:
                a = grid[row][col]
                for i in range(1,4):
                  a = a*grid[row + i*numpy.sign(walk1)][col + i*numpy.sign(walk2)]
                if a > s:
                  s = a

  print s
