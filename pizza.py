from sys import argv
from math import *

def slice_type(H, count = 0):
  x = floor(sqrt(H))
  y = H // x
  for i in range(0, count):
    if x > y:
      x -= 1
    else:
      y -= 1
  return x, y

def validate(slices, pizza):
  cells = 0
  for s in slices:
    cells += (s[2] - s[0] + 1) * (s[3] - s[1] + 1)
  m = len(pizza[0]) * len(pizza)
  return cells / m

if __name__ == "__main__":
  fname = 'example.in'
  if len(argv) == 2:
    fname = argv[1]

  with open(fname) as f:
    R, C, L, H = map(int, f.readline().split(' '))
    content = f.readlines()
    pizza = [list(x.strip()) for x in content]

  print(R, C, L, H)
  print(pizza)

  print(slice_type(H))

  slices = [[0, 0, 2, 1], [0, 2 ,2, 2], [0, 3, 2, 4]]
  nbr_slices = len(slices)
  print(validate(slices, pizza))
