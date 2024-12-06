import numpy as np

def quadroots(a, b, c):
    """
    Calculates the roots of the quadratic equation 0 = a*x^2 + b*x + c, and
    returns them as a tuple. If a root is repeated, the elements of the tuple
<<<<<<< HEAD

    will be identical. Hello!
=======
<<<<<<< HEAD
    will be identical. 

    **secret text** >:)
=======
    will be identical. Hello!
>>>>>>> 796e63c22f0d8d7c532f3d66cb278a1c0b3c0c97
>>>>>>> 773e995284710990696660b54d5063e6841e1a00
    

    ----------
    a: float
        Coefficient of x^2 in the input equation.
    b: float
        Coefficient of x in the input equation.
    c: float
        Constant coefficient of in the input equation.

    Returns
    -------
    (x1, x2): tuple<float>
        Roots of the equation.
    """

    x1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
    return (x1, x2)

