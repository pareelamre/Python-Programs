def count(sequence, item):
  total = 0
  for i in sequence:
    if i == item:
      total += 1
  return total

#same as: return sequence.count(item)
