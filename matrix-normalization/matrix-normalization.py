import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    try:
        A=np.array(matrix, dtype=float)

        if A.ndim!=2:
            return None

        if axis is None:

            if norm_type == 'l1':
                norm = np.sum(np.abs(A))

            elif norm_type == 'l2':
                norm = np.sqrt(np.sum(A**2))

            elif norm_type == 'max':
                norm = np.max(np.abs(A))

            else:
                return None

            if norm == 0:
                return A

            return A / norm

        
        if axis not in(0,1):
            return None
        
        if norm_type=='l1':
            norm=np.sum(np.abs(A),axis=axis,keepdims=True)
        elif norm_type=='l2':
            norm=np.sqrt(np.sum(A**2,axis=axis,keepdims=True))
        elif norm_type=='max':
            norm=np.max(np.abs(A),axis=axis,keepdims=True)
        else:
            return None

        norm[norm==0]=1 #To avoid div by 0
        
        result=A/norm

        return result
    except:
        return None
    

    