d = {
    0 : '',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
    100: 'hundred'
    }

def convert(i):
  if i < 21:
    return d[i]
  elif i < 100:
    return d[(i/10)*10] + d[i%10]
  elif i%100 == 0 and i < 1000:
    return d[i/100] + d[100]
  elif i < 1000:
    return d[i/100] + d[100] + 'and' + convert(i%100)
  elif i == 1000:
    return 'onethousand'

def solveit():
  s = 0
  for i in range(1, 1001):
    print i, convert(i)
    s += len(convert(i))
  print s

