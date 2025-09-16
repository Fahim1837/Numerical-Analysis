import sympy as sp

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def diff_nth(func, var, n):
    result = func
    for _ in range(n):
        result = sp.diff(result, var)
    return result

def taylors_theorem(func, k = 3, x0 = 0):
    result = 0
    x = sp.symbols('x')
    print(f"Applying Taylor's theorem to the function {func(x)} at x0 = {x0} up to degree {k}")
    for i in range(k + 1):
        term = (diff_nth(func(x), x, i).subs(x, x0) / factorial(i)) * (x - x0)**i
        result += term
        print(f"Degree {i}: {term}")
            
    # Print result in x first and then in numerical value
    print(f"Taylor's polynomial of degree {k} at x0 = {x0} evaluated at x = {x} is: {result}")
    print(f"Numerical value: {result}")
    return result

taylors_theorem(lambda x: sp.sin(x), k=5, x0=0)