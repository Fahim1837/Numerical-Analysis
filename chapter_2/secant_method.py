def secant_method(func, range, TOL=1e-5):
    a, b = range
    
    p = None
    p_n1 = (a + b) / 2.0
    p_n2 = (a + b) * (2.0 / 3.0)
    counter = 0
    
    print(f"{'Count':<8}|{'p':<15}|{'|p - p0|':<15}")
    print("-" * 35)
    
    while counter < 10:
        f_p1 = func(p_n1)
        f_p2 = func(p_n2)
        
        if p is None:
            diff_str = f"{'-':^10}"
        else:
            diff_str = f"{p:<10.7f}"
        
        print(f"{counter:<8}|{p:< 15.7f}|{diff_str}")
        
        if f_p2 - f_p1 == 0:
            print("\033[91mThe function values are equal. Hence the method fails.\033[0m")
            return None
        
        p = p_n1 - f_p1 * (p_n2 - p_n1) / (f_p2 - f_p1)
        
        if abs(p - p_n1) < TOL:
            return p_n1, counter
        
        p_n2 = p_n1
        p_n1 = p
        
        counter += 1
    
        if counter == 10:
            print("Warning: Maximum iterations reached without convergence.")
            return None
    
    