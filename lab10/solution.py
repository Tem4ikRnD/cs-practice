import numpy as np

def make_table(rows: int, columns: int) -> list[list[int]]:
    return np.arange(rows * columns).reshape(rows, columns).tolist()

def rectangle(
    matrix: list[list[float]],
    row_start: int,
    row_stop: int,
    column_start: int,
    column_stop: int
) -> list[list[float]]:
    arr = np.asarray(matrix)
    return arr[row_start:row_stop, column_start:column_stop].tolist()

def replace_rectangle(
    matrix: list[list[float]],
    row_start: int,
    row_stop: int,
    column_start: int,
    column_stop: int,
    value: float
) -> list[list[float]]:
    arr = np.asarray(matrix).copy()
    arr[row_start:row_stop, column_start:column_stop] = value
    return arr.tolist()

def matrix_vector_product(
    matrix: list[list[float]],
    vector: list[float]
) -> list[float]:
    return (np.asarray(matrix) @ np.asarray(vector)).tolist()

def matrix_multiply(
    left: list[list[float]],
    right: list[list[float]]
) -> list[list[float]]:
    return (np.asarray(left) @ np.asarray(right)).tolist()

def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    return np.asarray(matrix).T.tolist()

def solve_system(matrix: list[list[float]], vector: list[float]) -> list[float]:
    result = np.linalg.solve(np.asarray(matrix), np.asarray(vector))
    return np.round(result, 6).tolist()

def tensor_channel_mean(tensor: list) -> list:
    return np.asarray(tensor).mean(axis=-1).tolist()

def point_distance(first: list[float], second: list[float]) -> float:
    return round(np.linalg.norm(np.asarray(first) - np.asarray(second)), 6)