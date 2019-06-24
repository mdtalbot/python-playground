def printMove(from, to):
  print('Move from ' + str(from) + ' to ' + str(to) + '.')

def towers(n, from, to, spare):
  if n == 1:
    printMove(from, to)
  else:
    towers(n - 1, from, spare, to)
    towers(1, from, to, spare)
    towers(n -1, spare, to, from)

