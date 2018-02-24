class _Pizza_slice:
  def __init__(self, row, col, x, y):
    self.row = row
    self.col = col
    self.x = x
    self.y = y

    def get_pos():
      return self.x, self.y

    def get_dimensions():
      return self.row, self.col

    def set_x(self, i):
      self.x = i

    def set_y(self, i):
      self.y = i

    def set_row(self, i):
      self.row = i

    def set_col(self, i):
      self.col = i

    def getX():
      return self.x

    def getY():
      return self.y

    def getRow():
      return self.row

    def getCol():
      return self.col
