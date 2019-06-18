def remove_duplicates(lst):
  new = []
  for i in lst:
    if i not in new:
      new.append(i)
  return new    
