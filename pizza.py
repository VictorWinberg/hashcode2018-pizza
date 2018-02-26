from sys import argv
from math import floor, sqrt
from random import randint

class Pizza_slice():
  def __init__(self, width, height, x, y):
    self.width = width
    self.height = height
    self.x = x
    self.y = y

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

def validate_slice(ps, pizza, used, L):
  nbr_ing = { 'T': 0, 'M': 0 }
  for i in range(ps.y, ps.y + ps.height):
    for j in range(ps.x, ps.x + ps.width):
      if i < len(pizza) and j < len(pizza[0]) and used[i][j] == 0:
        nbr_ing[pizza[i][j]] += 1
      else:
        return False
  return nbr_ing['T'] >= L and nbr_ing['M'] >=L

def put_slice(ps, used, nbr) :
  for y in range(ps.x, ps.x + ps.width):
    for x in range(ps.y, ps.y + ps.height):
      used[x][y] = nbr
  return ps

def to_out(ps):
  return [ps.y, ps.x, (ps.y + ps.height - 1), (ps.x + ps.width - 1)]

def solve(pizza, R, C, L, H, seed):
  ps_nbr = 1
  squares_used = [[0 for x in range(C)] for y in range(R)]
  max_s = slice_types(H, R, C)
  slices = []
  for i in range(seed * R * C):
    x = randint(0, R)
    y = randint(0, C)
    s = randint(0, max_s)

    ps_width, ps_height = slice_type(H, R, C, s)
    ps = Pizza_slice(ps_width, ps_height, x, y)
    if validate_slice(ps, pizza, squares_used, L):
      slices.append(to_out(put_slice(ps, squares_used, ps_nbr)))
      ps_nbr += 1

  return validate(slices, pizza),slices

if __name__ == "__main__":
  fname = 'medium.in'

  count = 5
  seed = 10
  if len(argv) == 2:
    fname = argv[1]

  elif len(argv) == 4:
    fname = argv[1]
    count = int(argv[2])
    seed = int(argv[3])

  out_f = 'solution' + fname[:-3] + '.txt'

  with open(fname) as f:
    R, C, L, H = map(int, f.readline().split(' '))
    content = f.readlines()
    pizza = [list(x.strip()) for x in content]

  print(R, C, L, H)

  scores = {}
  for i in range(count):
    score, slices = solve(pizza, R, C, L, H, seed)
    scores[score] = slices
    if (count <= 20): # Just to see progress for big/medium
      print("Progress {}/{}".format(i + 1, count))

  m_score = max(scores, key=float)
  print(m_score)
  with open(out_f, 'w') as f:
    f.write(str(len(scores[m_score])) + '\n')
    for s in scores[m_score]:
      f.write(' '.join([str(a)  for a in s]) + '\n')
