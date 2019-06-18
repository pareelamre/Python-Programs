def digit_sum(n):
  s = 0
  while n != 0 :
    s = n % 10 + s
    n // 10
  print (s)
