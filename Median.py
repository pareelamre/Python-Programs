def median(lst):
  lst = sorted(lst)
  c = len(lst)
  if c % 2 == 0:
    index_1 = c/2 - 1
    index_2 = c/2
    med = (lst[index_1] + lst[index_2])/2.0
    return med
  else:
    index = c//2
    med = lst[index]
    return med
