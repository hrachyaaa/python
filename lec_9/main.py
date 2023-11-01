import random

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[random.randint(0, 100) for _ in range(columns)] for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            result.matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
            return result
        else:
            raise ValueError("Matrix sizes are different, can't apply addition operation!")

    def __sub__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            result.matrix = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
            return result
        else:
            raise ValueError("Matrix sizes are different, can't apply subtraction operation!")

    def __mul__(self, other):
        if self.columns == other.rows:
            result = Matrix(self.rows, other.columns)
            for i in range(self.rows):
                for j in range(other.columns):
                    result.matrix[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.columns))
            return result
        else:
            raise ValueError("Incorrect matrix sizes, can't apply multiplication operation!")

# Customize the matrices with your values
ob1 = Matrix(3, 3)
ob1.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"First object:\n{ob1}")

ob2 = Matrix(3, 3)
ob2.matrix = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(f"Second object:\n{ob2}")

try:
    print(f"Addition operation applied:\n{ob1 + ob2}")
except Exception as e:
    print(e)

try:
    print(f"Subtraction operation applied:\n{ob1 - ob2}")
except Exception as e:
    print(e)

try:
    print(f"Multiplication operation applied:\n{ob1 * ob2}")
except Exception as e:
    print(e)

