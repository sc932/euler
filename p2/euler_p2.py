def solveit():
  n1 = 0
  n2 = 1
  fib = 1
  a = 0
  while(1):
    fib = n1 + n2
    n1 = n2
    n2 = fib
    if fib > 4000000:
      break
    if fib%2 == 0:
      a += fib
  print a
