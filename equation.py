# Do NOT use any external libraries

def solve(A, b):
    """A is a m x n matrix, and b is an n x 1 vector.
    returns: x, where x is the solution to the equation Ax = b
    if no solution exists, return -1
    if infinite solutions exist, return -2"""
    x = [0] * len(A[0])
    m = len(A)
    n = len(A[0])
    if(m!=n):
        return -1
    for i in range(m):
        A[i].append(b[i][0])
    for i in range(n):
        maxrow = i
        for j in range(i+1,m):
            if(abs(A[j][i])>abs(A[maxrow][j])):
                maxrow = j
        temp = A[i]
        A[i] = A[maxrow]
        A[maxrow] = temp

        pivot = A[i][i]
        for j in range(n+1):
            A[i][j] = A[i][j]/pivot

        for j in range(m):
            if(j!=i):
                factor = A[j][i]
                for k in range(n+1):
                    A[j][k] = A[j][k] - factor*A[i][k]

    for i in range(m):
        iszero  = True
        for j in range(n):
            if(A[i][j]!=0):
                iszero = False
                break
        if(iszero and A[i][n]==0):
            return -2
        elif(iszero and A[i][n]!=0):
            return -1
        
        x = []
        for i in range(m):
            x.append(A[i][n])
        return x     

def swap_nonzero_row(A, l):
    
    for i in range(l+1, len(A)):
        if A[i][l] != 0:
            temp = A[l]
            A[l] = A[i]
            A[i] = temp
            return i
    return len(A)

def det(A):
    """calculates the determinant of A
    if A is not a square matrix, return 0"""
   
    if len(A) != len(A[0]):
        return 0
    A = [row[:] for row in A]  
    det = 1
    for l in range(len(A)):
        pivot = A[l][l]
        if pivot == 0:
            nl = swap_nonzero_row(A, l)
            if nl == len(A):
                det = 0
                return det
            else:
                pivot = A[l][l]
                det = det*(-1)
        det *= pivot
        for i in range(l+1, len(A)):
            factor = A[i][l] / pivot
            for j in range(l, len(A)):
                A[i][j] -= factor * A[l][j]
    return det
