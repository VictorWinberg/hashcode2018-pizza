from sys import argv
from math import *
from pizza_slice import _Pizza_slice

def slice_type(H, R, C, count = 0):
  x = floor(sqrt(H))
  y = H // x

  for i in range(0, count):
    if x == 2 and y == 2:
      x = min(H, R, C)
      y = 1
    elif x > y:
      x, y = y, x
    else:
      y -= 1
      if x == 1:
        x, y = y, x

  return x, y

def slice_types(H, R, C):
  count = 0
  while slice_type(H, R, C, count) != (1, 1):
    count += 1

  return count + 1

def validate(slices, pizza):
  cells = sum((s[2] - s[0] + 1) * (s[3] - s[1] + 1) for s in slices)
  m = len(pizza[0]) * len(pizza)
  return cells / m

def cnt_ing(ps, pizza, L):
  nbr_ing = {'T':0, 'M': 0}
  for i in range(ps.getX() + ps.getWidth):
    for j in range(ps.getY() + ps.getHeight()):
      if(i < len(pizza) and j < len(pizza[0])):
        nbr_ing[pizza[i][j]] += 1
      else:
        return False
  return nbr_ing['T'] >= L and nbr_ing['M'] >=L

def validate_pos(pizza_slice, used, nbr):
    for x in range(pizza_slice.getX(), pizza_slice.getX()+pizza_slice.getWidth()):
        for y in range(pizza_slice.getY(), pizza_slice.getY()+pizza_slice.getRow()):
            if(used[x, y] != 0):
                return False
    return True

def put_slice(pizza_slice, used, nbr) :
    for x in range(pizza_slice.getX(), pizza_slice.getX()+pizza_slice.getWidth()):
        for y in range(pizza_slice.getY(), pizza_slice.getY()+pizza_slice.getHeight()):
            used[x, y] = nbr
    nbr += 1


def try_slice(pizza_slice, pizza, used, nbr , L):
  return cnt_ing(pizza_slice, pizza, L) and validate_pos(pizza_slice, used, nbr)

def solve(pizza, R, C, L, H):
  slice_nbr = 1
  squares_used = [[0 for x in range(R)] for y in range(C)]
  for x in range(0, R):
    for y in range(0, C):
      for s in range(0, slice_types(H, R, C)):
        slice_width, slice_height = slice_type(H, R, C, s)
        ps = _Pizza_slice(slice_width, slice_height, x, y)
        if(try_slice(ps, pizza, squares_used, slice_nbr, L)):
          put_slice(ps, squares_used, slice_nbr)
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

  solve(pizza, R, C, L, H)
  slices = [[0, 0, 2, 1], [0, 2 ,2, 2], [0, 3, 2, 4]]

  print(validate(slices, pizza))
