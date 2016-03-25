#### Filename: MatrixFunctions.py

#### This program contains Matrix Arithmetic Functions

"""
Vector Functions

"""

def ScalarMult(s,V):
    return [i * s for i in V]

def AddVectors(S,T):
    if len(S) == len(T):
        return [S[i] + T[i] for i in range(len(S))]
    else:
        return ("The vectors are not compatible for multiplication")

def Dot(S,T):
    if len(S) == len(T):
        return sum([S[i] * T[i] for i in range(len(S))])
    else:
        return ("Vectors are not of equal number of components")

"""

Matrix Functions

"""


def showMatrix(mat):
    "Print out matrix"
    for row in mat:
        print(row)


def rows(mat):
    "return number of rows"
    return(len(mat))

def cols(mat):
    "return number of cols"
    return(len(mat[0]))
 

def GetCol(mat, col):
    return [row[col] for row in mat]
            
def Transpose(mat):
    # Create placeholder matrix (Original matrix will not be changed)
    mat_new = [[0] * len(mat) for k in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            # Assign transpose matrix elements
            mat_new[j][i] = mat[i][j]           
    return mat_new

def GetRow(mat, row):
    return mat[row]

def ScalarMultMatrix(a,mat):
    # Create placeholder matrix
    mat_new = [[0] * len(mat[0]) for k in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            # Multiply all elements with scalar
            mat_new[i][j] = a * mat[i][j]
    return mat_new

def AddMatrices(A,B):
    # Check if matrices are compatible
    if (len(A) == len(B)) & (len(A[0]) == len(B[0])):
            # Create placeholder matrix
            mat_new = [[0] * len(A[0]) for k in range(len(A))]
            for i in range(len(A)):
                for j in range(len(A[0])):
                    # Create new matrix out of the addition of two matrices.
                    mat_new[i][j] = A[i][j] + B[i][j]
            return mat_new
    else:
            return ("The matrices are not compatible for addition")

def MultiplyMat(mat1,mat2):
    # Check if matrices are compatible
    if len(mat1[0]) == len(mat2):
            # Create placeholder matrix
            mat_new = [[0] * len(mat2[0]) for l in range(len(mat1))]
            for i in range(len(mat1)):
                for j in range(len(mat2[0])):
                    # Create new matrix from multiplying rows and collumns.
                    mat_new[i][j] = sum([mat1[i][k] * mat2[k][j] for k in range(len(mat2))])
            return mat_new
    else:
            return ("The matrices are not compatible for multiplication")


######  Initial tests

A= [[4,-2,1,11],
    [-2,4,-2,-16],
    [1,-2,4,17]]

Ae= [[4,-2,1],
    [-2,4,-2],
    [1,-2,4]]


Bv=[11,-16,17]

Bm=[[11,-16,17]]

C=[2,3,5]

print("running matrixFunction.py file")

def testMatrix():
    print("A")
    showMatrix(A)
    print("Bm")
    showMatrix(Bm)
    print("Ae")
    showMatrix(Ae)
    print("multiplyMat(Ae,A)")
    showMatrix(MultiplyMat(Ae,A))
    print("scalarMultMatrix(2,A))")
    showMatrix(ScalarMultMatrix(2,A))
    print("addMatrices(A,A)")
    showMatrix(AddMatrices(A,A))
    print("transpose(A)")
    showMatrix(Transpose(A))

###  uncomment next line to run initial tests 
#testMatrix()
    
                   



