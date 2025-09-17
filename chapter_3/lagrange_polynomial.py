import sympy as sp
import numpy as np

def l_nk (points, n, k):
    x = sp.symbols('x')
    
    result = 1
    for i in range(n):
        if (i == k):
            continue
        term = (x - points[i][0])/(points[k][0] - points[i][0])
        result *= term

    return result
        
def lagrange_polynomial(points):
    n = points.shape[0]
    print(n)
    
    result = 0
    for i in range(n):
        l = l_nk(points, n ,i)
        # print (f"l:{i}, l: {l}")
        term = l * points[i][1]
        # print (f"term {i}: {term}")
        result += term
    
    print (f"Lagrange Polynomial of degree {n}: {result}")
    
    return result
    
# np_array = np.array([[0, 1], [1, 3], [2, 2], [3, 5], [4, 4], [5, 6]])
np_array = np.array([[2, 0.5], [2.75, 4/11], [4, 0.25]])
# np_array = np.array([[2,4], [5,1]])
x = lagrange_polynomial(np_array)
