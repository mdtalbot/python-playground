def vowel_counter(string):

  vowels = 'aeiou'
  counter = 0

  for i in string:
    if(i in vowels):
        counter += 1

  return("Number of vowels: " + str(counter))
