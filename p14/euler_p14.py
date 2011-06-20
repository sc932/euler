import numpy
def solveit():
  ms = 0
  winner = 0
  for i in range(2 ,1000001):
    num = i
    steps = 1
    seen = [num]
    while(1):
      steps += 1
      num = step(num)
      seen.append(num)
      if num == 1:
        #print i, seen, steps
        if steps > ms:
          ms = steps
          winner = i
        break
  print winner
     
    


def step(i):
  if i%2 == 0:
    return i/2
  else:
    return 3*i + 1

