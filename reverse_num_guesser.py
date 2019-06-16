def reverse_num_guesser():

  min = 0
  max = 100

  print("Please think of a number between 0 and 100!")
  while True:
      guess = (min + max) // 2
      print("Is your secret number " + str(guess) + '?')
      user_input = input(
          "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

      if user_input == 'c':
          print("Game over. Your secret number was " + str(guess) + '.')
          break
      elif user_input == 'h':
          max = guess
      elif user_input == 'l':
          min = guess
      else:
          print("Sorry, I did not understand your input.")
