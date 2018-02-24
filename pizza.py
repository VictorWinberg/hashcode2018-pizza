from sys import argv

if __name__ == "__main__":
  fname = 'example.in'
  if len(argv) == 2:
    fname = argv[1]

  with open(fname) as f:
    R, C, L, H = f.readline().split(' ')
    content = f.readlines()
    pizza = [x.strip() for x in content]

  print(R, C, L, H)
  print(pizza)