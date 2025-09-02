def bisection_method(func, args):
    a, b = args

    # Get the values for Intermediate Theorem
    f_a = func(a)
    f_b = func(b)

	# Initial settings
    p = 0
    counter = 0
    TOL = 10**(-4)
    f_p = func(p)

    result = a if f_a == 0 else (b if f_b == 0 else None)
    if result is not None:
        return result, counter

    # Check if Intermediate Theorem works
    if f_a * f_b < 0:
        a = a if f_a < 0 else b
        b = b if f_b > 0 else a
        p = (a + b) / 2.0
        f_p = func(p)
        counter = 1
            
    else:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    print(f"{'Count':<8}|{'a':<15}|{'b':<15}|{'p':<15}|{'abs(a-b)':<15}|{'f(p)':<15}")
    print("-" * 80)
    
    while abs(a - b) > TOL:
        print(f"{counter:<8}|{a:<15.5f}|{b:<15.5f}|{p:<15.5f}|{abs(a-b):<15.5e}|{f_p:>8.5f}")

        if f_p == 0:
            return p, counter

        # Ready for next iteration
        a = p if f_p < 0 else a
        b = p if f_p > 0 else b
        p = (a + b) / 2.0
        counter += 1
        f_p = func(p)

    return p, counter


bisection_method(lambda x: x**3 - x - 2, (1, 2))

