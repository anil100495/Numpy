# Matrix multiplication using loops
def multiply_loops(A,B):
    c=np.zeros((A.shape[0],B.shape[1]))
    for i in range(A.shape[1]):
        for j in range(B.shape[1]):
            c[i,j]= A[i,j] * B[j,i]
    return c
