import sympy as sp

def fixed_point_condition(func, range):
    a, b = range
    
    step_size = 0.1
    x = sp.symbols('x')
    print(f"Checking the function: {sp.simplify(func(x))} in the range [{a}, {b}]")
    dx = sp.diff(func(x), x)
    i = a
    
     
    # Check if the function has at least one fixed point
    while i <= b: 
        f_i = func(i)
        if f_i > b or f_i < a:
            print ("\033[91mThe function doesn't have a fixed point\033[0m")
            return None

        # The function f(i) must be continuous in [a, b]
        right_limit = sp.limit(func(x), x, i, dir='+')
        left_limit = sp.limit(func(x), x, i, dir='-')
        
        if right_limit != left_limit:
            print(f"\033[91mThe function has discontinuity at {i}. Hence f(x) is not continuous in [a, b]\033[0m")
            return None
        
        i += step_size
    
    print("\033[92mThe function has at least one fixed point in the given range.\033[0m")
    #  Check if the fixed point is unique
    i = a
    while i <= b:
        if abs(dx.subs(x, i)) >= 1:
            print(f"The function doesn't have a unique fixed point as |f'(x)| >= 1 at x = {i}")
            return None
        i += step_size
    
    print("\033[92mThe function has a unique fixed point in the given range.\033[0m")

def fixed_point_iteration(func, range, TOL = 1e-5):
    a, b = range

    # Initial settings
    p = (a + b) / 2.0
    counter = 0
    step_size = 0.1
        
    

    print(f"{'Count':<8}|{'p':<15}|{'f(p)':<15}")
    print("-" * 40)

    while True:
        print(f"{counter:<8}|{p:<15.7}|{f_p:>8.5f}")

        if abs(f_p) <= TOL:
            return p, counter

        # Ready for next iteration
        p = func(p)
        f_p = func(p)
        counter += 1
        
fixed_point_condition(lambda x: x**2, (0, 2))
fixed_point_condition(lambda x: ( x**2 - 1 ) / 3, (-1, 1))