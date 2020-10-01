import numpy as np
import os

curdir = os.path.dirname(os.path.abspath(__file__))
matrix_path = os.path.join(curdir, "{name}.npy")

trivial_board = {0: [1, 2, 3],
                 1: [0, 8],
                 2: [0, 6],
                 3: [0, 4],
                 4: [3, 5, 9],
                 5: [4, 6],
                 6: [2, 5, 7],
                 7: [6, 8],
                 8: [1, 7, 9],
                 9: [8, 4]
                }

die_values = [1, 2, 3, 4, 5, 6]


def check_matrix(matrix):
    for line in matrix:
        if round(line.sum())!=1:
            raise Exception("Error in matrix")
    print("[OK] Matrix")


def save_matrix(matrix, name):
    outfile = matrix_path.format(name=name)
    print(outfile)
    np.save(outfile, matrix)


def load_matrix(name):
    outfile = matrix_path.format(name=name)
    return np.load(outfile)


if __name__ == '__main__':
    matrix = np.zeros((10,10))

    # init matrix for die shows a 1
    for pos in range(10):
        for next_pos in trivial_board[pos]:
            val = 1 / len(trivial_board[pos])
            matrix[pos][next_pos] = val
    check_matrix(matrix)
    save_matrix(matrix, "matrix_d1")

    matrix_d1 = matrix.copy()
    for die in die_values[1:]:
        matrix = np.dot(matrix, matrix_d1)
        check_matrix(matrix)
        save_matrix(matrix, "matrix_d%d" % die)