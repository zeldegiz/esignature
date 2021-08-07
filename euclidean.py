def euclidean_calculator(a,b):
  assert a > b, 'a must be larger than b'
  x0, x1, y0, y1 = 1, 0, 0, 1
  while a != 0:
    q, b, a = b // a, a, b % a
    x0, x1 = x1, x0 - q * x1
    y0, y1 = y1, y0 - q * y1
  return  b, y0, x0