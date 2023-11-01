class CustomMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def display(self):
        for row in self.data:
            print(row)

    def find_mean(self):
        total = sum(sum(row) for row in self.data)
        return total / (self.rows * self.cols)

    def calculate_row_total(self, row_idx):
        if 0 <= row_idx < self.rows:
            return sum(self.data[row_idx])
        else:
            return None

    def calculate_column_avg(self, col_idx):
        if 0 <= col_idx < self.cols:
            total = sum(row[col_idx] for row in self.data)
            return total / self.rows
        else:
            return None

    def display_submatrix(self, indices):
        col_start, col_end, row_start, row_end = indices
        if 0 <= col_start < col_end <= self.cols and 0 <= row_start < row_end <= self.rows:
            submatrix = [row[col_start:col_end] for row in self.data[row_start:row_end]]
            for row in submatrix:
                print(row)
        else:
            print("Invalid submatrix indices.")

n = 4
m = 3
my_matrix = CustomMatrix(n, m)

my_matrix.data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

print("Matrix:")
my_matrix.display()

mean_value = my_matrix.find_mean()
print(f"Mean of the matrix: {mean_value}")

row_sum_result = my_matrix.calculate_row_total(2)
if row_sum_result is not None:
    print(f"Sum of row 2: {row_sum_result}")
else:
    print("Invalid row index.")

column_avg = my_matrix.calculate_column_avg(1)
if column_avg is not None:
    print(f"Average of column 1: {column_avg}")
else:
    print("Invalid column index.")

print("Submatrix:")
my_matrix.display_submatrix([1, 3, 0, 2])

