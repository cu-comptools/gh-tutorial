import numpy as np
from quadutils import quadroots as qr
from quadutils import chebutils as ch

def test_quadroots_1():
    a = 1.0
    b = -3.0
    c = 2.0
    roots = qr.quadroots(a, b, c)
    x1_exact = 2.0
    x2_exact = 1.0
    assert (np.abs(roots[0] - x1_exact) < 1e-14) and (np.abs(roots[1] - x2_exact)) < 1e-14 

def test_chebD_1():
    n = 16
    D, x = ch.chebD(n) 
    print(x)
    f = lambda x: x**2 # Test function should be differentiated exactly
    interval = np.array([0, 0.5])
    h = interval[1] - interval[0]
    x_scaled = (x+1)/2*h + interval[0]
    df_ana = lambda x: 2*x
    df_num = 2/h*D@f(x_scaled)
    df_err = max(np.abs(df_ana(x_scaled) - df_num))
    assert df_err < 1e-13

def test_phi_1():
    pass
