from sys import argv
from math import *
from pizza_slice import Pizza_slice
from random import randint, uniform

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
  nbr_ing = {'T': 0, 'M': 0}
  for i in range(ps.x, ps.x + ps.width):
    for j in range(ps.y, ps.y + ps.height):
      if(i < len(pizza) and j < len(pizza[0])):
        nbr_ing[pizza[i][j]] += 1
      else:
        return False
  return nbr_ing['T'] >= L and nbr_ing['M'] >=L

def validate_pos(ps, used, nbr):
  for x in range(ps.x, ps.x + ps.width):
    for y in range(ps.y, ps.y + ps.height):
      if(used[x][y] != 0):
        return False
  return True

def try_slice(ps, pizza, used, nbr , L):
  return cnt_ing(ps, pizza, L) and validate_pos(ps, used, nbr)
def put_slice(ps, used, nbr) :
  for x in range(ps.x, ps.x + ps.width):
    for y in range(ps.y, ps.y + ps.height):
      used[x][y] = nbr
  return ps

def translate(slices):
  out_slices = []
  for s in slices:
    out_slices.append([s.x, s.y, (s.x + s.width),(s.y + s.height)])
  print(out_slices)
  return out_slices

def solve(pizza, R, C, L, H):
  slice_nbr = 1
  squares_used = [[0 for x in range(C)] for y in range(R)]
  max_s = slice_types(H, R, C)
  slices = []
  for i in range(100 * R * C):
    x = randint(0, R)
    y = randint(0, C)
    s = randint(0, max_s)

    slice_width, slice_height = slice_type(H, R, C, s)
    ps = Pizza_slice(slice_width, slice_height, x, y)
    if(try_slice(ps, pizza, squares_used, slice_nbr, L)):
      slices.append(put_slice(ps, squares_used, slice_nbr))
      slice_nbr += 1

  out_slices = translate(slices)
  return validate(out_slices, pizza),out_slices

if __name__ == "__main__":
  fname = 'example.in'
  count = 100
  if len(argv) == 2:
    fname = argv[1]


  with open(fname) as f:
    R, C, L, H = map(int, f.readline().split(' '))
    content = f.readlines()
    pizza = [list(x.strip()) for x in content]

  print(R, C, L, H)
  print(pizza)
  scores = {}
  for i in range(count):
    score, slices = solve(pizza, R, C, L, H)
    scores[score] = slices
  print(scores[max(scores, key=float)], max(scores, key=float))

  slices = [[0, 0, 2, 1], [0, 2 ,2, 2], [0, 3, 2, 4]]

  print(validate(slices, pizza))
