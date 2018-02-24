from sys import argv

def try_slice():
    return true


if __name__ == "__main__":
  fname = 'example.in'
  if len(argv) == 2:
    fname = argv[1]

  with open(fname) as f:
    R, C, L, H = map(int, f.readline().split(' '))
    content = f.readlines()
    pizza = [list(x.strip()) for x in content]

    for x in range(0, R):
        for y in range(0, C):
            for s in range(0, 1):  #1 ska ändras till hur många gånger man kan kalla på try_slices
                if(try_slice(x, y, slice_type(H, s)))
                    put_slice()


  print(R, C, L, H)
  print(pizza)
