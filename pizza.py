from sys import argv
from math import *

class _Pizza_slice:
    def __init__(self, row, col, x, y):
        self.row = row
        self.col = col
        self.x = x
        self.y = y
        def get_pos():
            return self.x, self.y;
        def get_dimensions():
            return self.row, self.col;
        def set_x(self, i):
            self.x = i
        def set_y(self, i):
            self.y = i
        def set_row(self, i):
            self.row = i
        def set_col(self, i):
            col = i
        def getX():
            return self.x;
        def getY():
            return self.y;
        def getRow():
            return self.row;
        def getCol():
            return self.col;


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

def try_slice():
    return true
def put_slice(pizza_slice, used, nbr) :
    for x in range(pizza_slice.getX(), pizza_slice.getX()+pizza_slice.getRow()):
        used[x] = nbr
    for x in range(pizza_slice.getY(), pizza_slice.getY()+pizza_slice.getCol()):
        squares_used[y] = nbr
    nbr++

if __name__ == "__main__":
  fname = 'example.in'
  if len(argv) == 2:
    fname = argv[1]

  with open(fname) as f:
    R, C, L, H = map(int, f.readline().split(' '))
    content = f.readlines()
    pizza = [list(x.strip()) for x in content]


  slice_nbr = 1;
  squares_used = [[0 for x in range(R)] for y in range(C)]
    for x in range(0, R):
        for y in range(0, C):
            for s in range(0, 1):  #1 ska ändras till hur många gånger man kan kalla på try_slices
                ps = Pizza_slice(slice_type(H, s, x, y))
                if(try_slice(ps, squares_used, slice_nbr)):
                    put_slice()

  print(R, C, L, H)
  print(pizza)


  print(slice_type(H))

  slices = [[0, 0, 2, 1], [0, 2 ,2, 2], [0, 3, 2, 4]]
  nbr_slices = len(slices)
  print(validate(slices, pizza))
