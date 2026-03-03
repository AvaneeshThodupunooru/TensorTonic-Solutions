import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x=np.asarray(x,dtype=float)
    q=np.asarray(q,dtype=float)

    if x.size==0:
        raise ValueError("Input array X must have at least one element")
    if np.any((q<0)|(q>100)):
        raise ValueError("Percentiles q must be in range [0, 100]")

    x_srted=np.sort(x)
    result = np.percentile(x_srted,q,method='linear')
    return np.asarray(result)
        
    
        
    
    