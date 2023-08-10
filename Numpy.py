# Matrix multiplication using loops
def multiply_loops(A,B):
    c=np.zeros((A.shape[0],B.shape[1]))
    for i in range(A.shape[1]):
        for j in range(B.shape[1]):
            c[i,j]= A[i,j] * B[j,i]
    return c
# use of inbuit numpy fun @ for mtarix multiplication  
def multiply_vector(A,B):
    return A @ B    # @ internal function provided by Numpy 
