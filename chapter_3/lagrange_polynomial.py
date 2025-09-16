import sympy as sp

def define_L_nk(n=5, k=3):
    x = sp.symbols('x')
    result = 1
    for i in range(n + 1):
        if i == k:
            continue
        else:
            term = (x - i) / (k - i)
            result *= term
    print("L_{n,k}(x) =", result)
    return result

def lagrange_polynomial(func, n=5):
    x = sp.symbols('x')
    result = 0
    print(f"Constructing Lagrange polynomial of degree {n} for the function {func(x)}")
    for k in range(n + 1):
        L_nk = define_L_nk(n, k)
        term = func(k) * L_nk
        result += term
        print(f"Term for k={k}: {term}")
    
    # Print result in x first and then in numerical value
    print(f"Lagrange polynomial of degree {n} is: {result}")
    print(f"Numerical value: {result}")
    return result