def solveit():
  primes = [2]
  num = 3
  true = 600851475143
  while(1):
    fail = False
    for pr in primes:
      if num%pr == 0:
        fail = True
    if fail == False:
      if true%num == 0:
        if true == num:
          print true
          break
        else:
          true = true/num
          print true
      primes.append(num)
    num += 2
  print primes[-1]
