import numpy as np
import scipt as sp

def Phi(x, y, k = 0.0):
    """
    Determines the distance between all pairs of point of two vectors the with the same size in the first dimension and     having any size for the second dimension

    Parameters
    ----------
    x: np.array<float>
        Can have shape (2, n) or (2,). In the latter case, it'll be converted
        to (2, 1)
    y:  Can have shape (2, m) or (2,). In the latter case, it'll be converted
        to (2, 1).
    k: float, optional
        Default k = 0. A constant in the fundamental soln

    Returns
    -------
    phi: np.array<float> 
        Has size (m,n). The fundamental solution. 
    """

    # Reshape input vectors if given in the shape (2,). Skip if (2, n).
    if x.ndim < 2: 
        x = x.reshape((2, -1))#change array so 2 entries and the rest on the other axis
    if y.ndim < 2:
        y = y.reshape((2, -1))
    # Distance vector(s) between pairs of (x, y). 
    # If x is (2, n), and y is (2, m), d will still be of shape (2, n, m).
    d = x[..., None] - y[:, None]
    if k == 0.0:
        phi = -1/(2*np.pi)*np.log(np.linalg.norm(d, axis = 0))
    else:
        r = np.linalg.norm(d, axis = 0)
        phi = 1j/4*sp.hankel1(0, k*r)
    return phi
    
