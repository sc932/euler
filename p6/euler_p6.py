def solveit():
  a = 0
  b = 0
  for i in range(1,101):
    b += i*i
    a += i
  print a
  print b
  print a*a - b
