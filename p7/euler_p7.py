def solveit():
  primes = [2]
  num = 3
  while(len(primes) != 10001):
    fail = False
    for pr in primes:
      if num%pr == 0:
        fail = True
    if fail == False:
      primes.append(num)
    num += 2
  print primes[-1]
