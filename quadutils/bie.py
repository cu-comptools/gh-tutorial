import numpy as np

import scipy as sp

def Phi(x, y, k = 0.0):
    """
    Computes the fundamental solution of the Helmholtz equation (if the
    wavenumber k is not 0) or the Laplace equation in 2D, at position(s) x with
    source(s) y.


    Parameters
    ----------
    x: np.array<float>
        Can have shape (2, n) or (2,). In the latter case, it'll be converted
        to (2, 1).

        Position vector(s) pointing to the target(s).
    y: np.array<float>
        Can have shape (2, m) or (2,). In the latter case, it'll be converted
        to (2, 1).
        Position vector(s) pointing to the source(s).
    k: float, optional
        Default k = 0. Wavenumber; if zero then the Laplace fundamental
        solution will be computed.

    Returns
    -------
    phi: np.array<complex<float>> 
        Has shape (n, m). Array of fundamental solutions for target and source pair(s).
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
    
