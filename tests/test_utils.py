import numpy as np
from quadutils import quadroots as qr

def test_quadroots_1():
    a = 1.0
    b = -3.0
    c = 2.0
    roots = qr.quadroots(a, b, c)
    x1_exact = 2.0
    x2_exact = 1.0
    assert (np.abs(roots[0] - x1_exact) < 1e-14) and (np.abs(roots[1] - x2_exact)) < 1e-14 

