import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    v=np.array(v)
    n=v.size
    diagonal=np.zeros((n,n),dtype=v.dtype)
    for i in range(n):
        diagonal[i,i]=v[i]
    return diagonal
    