def solveit():
  fibCur = 1
  fibPrev = 1
  term = 2
  while(len(str(fibCur)) < 1000):
    temp = fibCur
    fibCur = fibCur + fibPrev
    fibPrev = temp
    term += 1
  print term
