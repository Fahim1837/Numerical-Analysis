def bisection_method(func, range, TOL = 1e-4):
    a, b = range

    # Get the values for Intermediate Theorem
    f_a = func(a)
    f_b = func(b)

	# Initial settings
    p = 0
    counter = 0
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
    
    while True:
        print(f"{counter:<8}|{a:<15.5f}|{b:<15.5f}|{p:<15.7}|{abs(a-b):<15.5e}|{f_p:>8.5f}")

        if abs(a - b) <= TOL:
            return p, counter
        
        if f_p == 0:
            return p, counter

        # Ready for next iteration
        a = p if f_p < 0 else a
        b = p if f_p > 0 else b
        p = (a + b) / 2.0
        counter += 1
        f_p = func(p)

p = bisection_method(lambda x: x**3 + 4*x**2 - 10, (1,2))
print(f"Final Result: {p[0]}")
