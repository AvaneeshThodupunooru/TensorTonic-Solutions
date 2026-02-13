import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x=np.array(x,dtype=float)
    y=np.array(y,dtype=float)

    if x.ndim!=1 or y.ndim!=1:
        raise ValueError("Only 1D arrays allowed")

    if x.shape[0]!= y.shape[0]:
        raise ValueError("Vectors not of same length")

    result=np.dot(x,y)
    return float(result)