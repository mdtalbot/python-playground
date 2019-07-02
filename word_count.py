def word_count(passage):
  newDict = {}
  for word in passage:
    if word in newDict:
      newDict[word] += 1
    else:
      newDict[word] = 1
  return newDict
