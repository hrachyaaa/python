import random

def generate_random_matrix(num_rows, num_columns):
    matrix = []
    for _ in range(num_rows):
        row = [random.randint(1, 100) for _ in range(num_columns)]
        matrix.append(row)
    return matrix

def calculate_column_sum(matrix, column_idx):
    if column_idx < 0 or column_idx >= len(matrix[0]):
        return None
    column_sum = 0
    for row in matrix:
        column_sum += row[column_idx]
    return column_sum

def calculate_row_average(matrix, row_idx):
    if row_idx < 0 or row_idx >= len(matrix):
        return None
    row = matrix[row_idx]
    row_average = sum(row) / len(row)
    return row_average

num_rows = 4
num_columns = 3
matrix = generate_random_matrix(num_rows, num_columns)
print("Generated Matrix:")
for row in matrix:
    print(row)

column_idx = 1
column_sum = calculate_column_sum(matrix, column_idx)
if column_sum is not None:
    print(f"Sum of column {column_idx}: {column_sum}")
else:
    print(f"Invalid column index: {column_idx}")

row_idx = 2
row_average = calculate_row_average(matrix, row_idx)
if row_average is not None:
    print(f"Average of row {row_idx}: {row_average}")
else:
    print(f"Invalid row index: {row_idx}")

