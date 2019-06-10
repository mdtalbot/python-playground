def alpha_order_substring(str):

  previous_char = ""
  current_string = ""
  max_string = ""

  for i in str:
    if previous_char <= i:
        current_string += i
        if len(current_string) > len(max_string):
            max_string = current_string
    else:
        current_string = i
    previous_char = i
  print('Longest substring in alphabetical order is: ' + max_string)
