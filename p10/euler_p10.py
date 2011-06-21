def solveit():
  print sum(getPrimes(2000000)) 

def getPrimes(n):
  primes = list(range(n+1))
  primes[1] = 0
  for i in range(2,len(primes)):
    if primes[i] != 0:
      cullMult = 2
      while(cullMult*i < len(primes)):
        primes[cullMult*i] = 0
        cullMult += 1
  return primes
