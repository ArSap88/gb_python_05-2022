class Matrix:
    def __init__(self, list_1):
        self.list_1 = list_1

    def __str__(self):
        for row in self.list_1:
            for i in row:
                print(f'{i:5}', end='')
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.list_1)):
            for j in range(len(other.list_1[i])):
                self.list_1[i][j] = self.list_1[i][j] + other.list_1[i][j]
            return Matrix.__str__(self)


matrix = Matrix([[1, 2], [2, 3], [4, 5]])
new_matrix = Matrix([[-1, -2], [-2, -3], [-4, -5]])
print(matrix + new_matrix)
