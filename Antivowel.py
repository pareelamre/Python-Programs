def anti_vowel(text):
  new = ''
  for c in text:
    if c not in "aeiouAEIOU":
      new += c
  return new    
