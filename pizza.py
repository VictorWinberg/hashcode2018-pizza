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
