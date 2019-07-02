def most_common_words(freqs):
  values = freqs.values()
  highest = max(freqs.values())
  words = []
  for k in freqs:
    if freqs[k] == highest:
      words.append(k)
  return (words, highest)
