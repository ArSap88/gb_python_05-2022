class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        if isinstance(other, Cell):
            return self.quantity + other.quantity

    def __sub__(self, other):
        if isinstance(other, Cell) and self.quantity - other.quantity > 0:
            return self.quantity - other.quantity

    def __truediv__(self, other):
        if isinstance(other, Cell):
            return self.quantity // other.quantity

    def __mul__(self, other):
        if isinstance(other, Cell):
            return self.quantity * other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


object_cell_1 = Cell(15)
object_cell_2 = Cell(5)
print(f'+: {object_cell_1 + object_cell_2} '
      f'\n-: {object_cell_1 - object_cell_2} '
      f'\n*: {object_cell_1 * object_cell_2} '
      f'\n/: {object_cell_1 / object_cell_2}'
      f'\n{object_cell_1.make_order(5)}')
