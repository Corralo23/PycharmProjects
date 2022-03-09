import mat as mat
import matrices as matrices


def matrix_sum(*matrices):
    mat = matrices[0]

for matrix in matrices[1:]:
    for x, row in enumerate(matrix):
        for y, col in enumerate(row):
            mat[x][y] += col
              return mat

def camel_case(s):
    return "".join(s.title().split())

if __name__ == '__main__':

    print(matrix_sum([[1, 2], [3, 4]], [[5, 6], [7,8]]))
    print(camel_case('close to the edge'))

