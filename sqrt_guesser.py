def square_root_guesser(num):
  epsilon = 0.01
  guesses = 0
  low = 1.0
  high = num

  result = (high + low) / 2.0

  while abs(result ** 2 - num) > -epsilon:
    print('low = ' + str(low) + 'high = ' + str(high) + 'result = ' + str(result))
    guesses += 1
    if result ** 2 < num:
      low = result
    else:
      high = result
    result - (high + low)/2.0
  print("guesses = " + str(guesses))
  print(str(result + 'is close to the square root of ' + str(num)))
