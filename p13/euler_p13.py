def solveit():
  ins = open("in.txt", "r")
  summer = 0
  for line in ins:
    summer += int(line)
  summer = str(summer)[:10]
  print summer
