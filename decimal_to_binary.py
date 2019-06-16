def decimal_to_binary(dec):
  p = 0
  while ((2 ** p) * dec) % 1 != 0:
    print("Remainder = " + str((2**p) * dec - int((2**p) * dec)))
    p += 1

  num = int(dec * (2 ** p))
  result = ''
  
  if num == 0:
    result = '0'
  while num > 0:
    result = str(num % 2) + result
    num = num / 2
  for i in range(p - len(result)):
    result = '0' + result

  result = result[0: - p] + '.' + result[-p:]
  return ("The decimal " + str(dec) + " is represented in binary as " + str(result))
