def substring_finder(str, ss):

  counter = 0
  ss_len = len(ss)

  for i in range(len(str)):
    if str[i:i+ss_len] == ss:
        counter += 1
    print(counter)
