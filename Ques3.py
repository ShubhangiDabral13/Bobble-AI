def create_zero(mat):
    #creating 2 dictonaries for rows and columns
    row = {}
    col = {}
    #finding the number rows and columns in matrix
    r = len(mat)
    c = len(mat[0])

    #Loop through each element in a given matrix and check whether it is zero or not.
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 0:
                if row.get(i) == None:
                    row[i] = True
                if col.get(j) == None:
                    col[j] = True

    #making those columns zero whose corressponding rows are zero in matrix.
    for i in row.keys():
        for j in range(0, c):
            mat[i][j] = 0

    #making those rows zero whose corressponding colums are zero in matrix.
    for i in col.keys():
        for j in range(0, c):
            mat[j][i] = 0

    return mat

## inputmatrix
mat = [
  [0, 1],
  [1, 0]
]

print(create_zero(mat))

##Output
"""
[[0, 0], [0, 0]]

"""
