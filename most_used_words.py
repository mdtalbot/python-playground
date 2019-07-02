import most_common_words

def most_used_words(freqs, minTimes):
  result = []
  done = False
  while not done:
      temp = most_common_words(freqs)
      if temp[1] >= minTimes:
        result.append(temp)
        for w in temp[0]:
          del (freqs[w])
      else:
        done = True
  return result

