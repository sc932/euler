def solveit():
  i = 20
  while(1):
    i += 20
    if isSuperDiv(i):
      print i
      break


def isSuperDiv(x):
  for i in range(2,20):
    if x%i != 0:
      return False
  return True
