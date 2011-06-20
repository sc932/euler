def solvit():
  a = range(1000)
  a.reverse()
  # ugly
  m = -1
  for i in a:
    for j in a:
      if isPal(i*j):
        if i*j > m:
          m = i*j
  print m

def isPal(a):
  s = str(a)
  for i in range(len(s)/2):
    if s[i] != s[len(s) - i - 1]:
      return False
  return True
