#### Filename: MatrixInverse.py

#### This program gets the Inverse of a matrix.

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
        
def identity(n):
    "creates nxn identity matrix"
    return [[0 if col != row else 1 for col in range(n)] for row in range(n)]

def augmentMat(mat1, mat2):
    amat = []
    for i in range(rows(mat1)):
        amat.append(mat1[i] + mat2[i])
    return amat

# Function source: https://rosettacode.org/wiki/Reduced_row_echelon_form#Python
def ToReducedRowEchelonForm(M):
    if not M: return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        M[r] = [ mrx / float(lv) for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
        lead += 1
    return M
        
def getInverse(mat):
    # Check if matrix is compatible
    if len(mat[0]) == len(mat):
        # Placeholder matrix
        mat_new = [[0] * len(mat)for l in range(len(mat))]
        I_new = [[0] * len(mat)for l in range(len(mat))]
        I = identity(len(mat))
        A = augmentMat(mat,I)
        ToReducedRowEchelonForm(A)
        # START: NOT PART OF ALGORITHM, ONLY FOR CONVIENIENCE
        # Extract inverse from matrix from augmented matrix
        for i in range(len(mat)):
            for j in range(len(mat)):
                mat_new[i][j] = A[i][j + len(mat)]
        # Extract row reduced identity from augmented matrix
        for i in range(len(I)):
            for j in range(len(I)):
                I_new[i][j] = A[i][j]
        # END: CONVIENIENCE EXTRACTIONS
        # Check if matrix inverse valid
        if (I == I_new):
            return mat_new
        else:
            print ("The matrix does not have a inverse, returning identity: \n")
            return identity(len(mat))
    else:
        print ("The matrix does not have a inverse, returning identity: \n")
        return identity(len(mat))
            
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

def printInverse(M):
    print ("\n****************************\nINVERSE\n****************************")
    b = [[1],[2],[3]]
    print ("To find the inverse of Matrix: \n")
    showMatrix(M)
    print ("\nWe first augment the Matrix with it's identity. Thus we have, \n[A|I], where A = Matrix and I = Identity\n")
    I = identity(len(M))
    A = augmentMat(M,I)
    showMatrix(A)
    print ("\nAfter applying the reduced row echelon algorithm, we can obtain the new augmented matrix [I|A**-1]\n")
    ToReducedRowEchelonForm(A)
    showMatrix(A)
    print ("\nThus, we can extract the inverse of A: \n")
    inverse = getInverse(M)
    showMatrix(inverse)
    print ("\nIf we had a b vector of: \n")
    showMatrix(b)
    print ("\nWe can calculate the x vector by multiplying the inverse of A with the b vector.")
    print ("Therefore, we get the answer for the x vector: \n")
    x = MultiplyMat(inverse, b)
    showMatrix(x)

# Change M to the Matrix you want to get the inverse of
M = [[4,-2,1],
    [-2,4,-2],
    [1,-2,4]]

printInverse(M)


 
