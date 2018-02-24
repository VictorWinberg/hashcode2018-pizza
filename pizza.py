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

def cnt_ing(x, y, slice_x, slice_y, pizza, L):
  nbr_ing = {}
  nbr_ing['T'] = 0
  nbr_ing['M'] = 0
  for i in range(x + slice_x):
    for j in range(y + slice_y):
      if(i < len(pizza) and j < len(pizza[0])):
        nbr_ing[pizza[i][j]] += 1
      else:
        return False
  return nbr_ing['T'] >= L and nbr_ing['M'] >=L

def try_slice(x, y, slice_x, slice_y, pizza, L):
  return cnt_ing(x, y, slice_x, slice_y, pizza, L)

def solve(pizza, R, C, L, H):
  for x in range(0, R):
    for y in range(0, C):
      for s in range(0, 1):  #1 ska ändras till hur många gånger man kan kalla på try_slices
        slice_x, slice_y = slice_type(H, s)
        if(try_slice(x, y, slice_x, slice_y, pizza, L)):
          # put_slice()
          x += 0
          y += 0


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
  solve(pizza, R, C, L, H)
  slices = [[0, 0, 2, 1], [0, 2 ,2, 2], [0, 3, 2, 4]]
  nbr_slices = len(slices)
  print(validate(slices, pizza))
