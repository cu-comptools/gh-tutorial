import numpy as np
#import scipy.integrate as si

def chebD(n):
    """
    Computes the (n+1)x(n+1) spectral differentiation matrix\
    using Chebyshev roots according to Ch 6 of Trefethen's\
    "Spectral methods in MATLAB". Returns D and nodes on [-1, 1].
    Note that they are ordered backwards, i.e. 1 to -1!

    Parameters
    ----------
    n: int
        number of Chebyshev nodes - 1.

    Returns
    -------
    D: np.array<float>
        (n+1) x (n+1) Chebyshev differentiation matrix
    x: np.array<float>
        (n+1)-length vector of Chebyshev nodes, ordered from 1 to -1.
    """
    if n == 0:
        x = 1; D = 0; w = 0
    else:
        a = np.linspace(0.0, 2*np.pi, n+1)
        x = np.cos(a)
        b = np.ones_like(x)
        b[0] = 2; b[-1] = 2
        d = np.ones_like(b)
        d[1::2] = -1
        c = b*d
        X = np.outer(x, np.ones(n+1))
        dX = X - X.T
        D = np.outer(c, 1/c) / (dX + np.identity(n+1))
        D = D - np.diag(D.sum(axis=1))
    return D, x
