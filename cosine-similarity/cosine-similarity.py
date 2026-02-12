import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a=np.array(a)
    b=np.array(b)
    dotp=np.dot(a,b)
    anorm=np.linalg.norm(a)
    bnorm=np.linalg.norm(b)
    tnorm=anorm*bnorm
    return 0.0 if tnorm==0 else dotp/tnorm
    