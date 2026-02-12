import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A=np.array(A)
    n=A.shape[1]
    Sum=0
    for i in range(n):
        Sum+=A[i,i]
    return Sum

    
