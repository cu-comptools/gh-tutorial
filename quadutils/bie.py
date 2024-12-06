import numpy as np

import scipy as sp

def Phi(x, y, k = 0.0):
    """
    What does this function do?


    Parameters
    ----------
    x: np.array<float>
        Can have shape (2, n) or (2,). In the latter case, it'll be converted
        to (2, 1).
        What is this variable? spatial points inside the domain of interest
    y: np.array<float>
        Can have shape (2, m) or (2,). In the latter case, it'll be converted
        to (2, 1).
        What is this variable? points on boundary of the domain of interest
    k: float, optional
        Default k = 0. What is this variable? parameter in the Helmholtz

    Returns
    -------
    phi: ? 

        What's this variable? What's its shape? np.array<float>, fundamental solution to the Helmholtz equation, evaluated at x,y. it should be n*m x 1, or something like this. 

    """
    # Reshape input vectors if given in the shape (2,). Skip if (2, n).
    if x.ndim < 2: 
        x = x.reshape((2, -1))
    if y.ndim < 2:
        y = y.reshape((2, -1))
    # Distance vector(s) between pairs of (x, y). 
    # If x is (2, n), and y is (2, m), d will still be of shape (2, n, m).
    d = x[..., None] - y[:, None]

    # What are these two cases?
    if k == 0.0:
        phi = -1/(2*np.pi)*np.log(np.linalg.norm(d, axis = 0))
    else:
        r = np.linalg.norm(d, axis = 0)
        phi = 1j/4*sp.hankel1(0, k*r)
    return phi
    
