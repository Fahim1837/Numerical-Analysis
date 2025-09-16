import sympy as sp
def newtonian_method(func, range, TOL = 1e-5):
    a, b = range

    # Initial settings
    p = (a + b) / 2.0
    p_prev = None
    counter = 0
    x = sp.symbols("x")
    dx = sp.diff(func(x), x)

    print(f"{'Count':<8}|{'p':<15}|{'|p - p0|':<15}")
    print("-" * 35)

    # Iterating the Loop
    while counter < 10:
        # show '-' for the initial previous value
        if p_prev is None:
            diff_str = f"{'-':^10}"
        else:
            diff_str = f"{abs(p - p_prev):<10.7f}"

        print(f"{counter:<8}|{p:< 15.7f}|{diff_str}")

        if abs(func(p)) < TOL:
            return p, counter

        if dx.subs(x, p) == 0:
            print("\033[91mThe derivative is zero. Hence the method fails.\033[0m")
            return None

        # Ready for next iteration
        p_prev = p
        p = p_prev - func(p_prev) / dx.subs(x, p_prev)
        counter += 1

    return p, counter

newtonian_method(lambda x: x**3 + 4*x**2 - 10, (1,2))