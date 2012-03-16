
def bisect(f, a, b, tol):
    """ given a function f, find a root between a and b with tolerence of tol"""
    
    f_a = f(a)
    f_b = f(b)

    return bisect1(f, f_a, f_b, a, b, tol)

def bisect1(f, f_a, f_b, a, b, tol):
    """ given a function f, find a root between a and b with tolerence of tol"""

    c = 0.5*(a + b)
    f_c = f(c)
    
    if abs(f_c) < tol:
        return c
            
    if f_a * f_c < 0: # root between a and b
        return bisect1(f, f_a, f_c, a, c, tol)
    else:
        return bisect1(f, f_c, f_b, c, b, tol)
            
def simple_x1(x):
    return x - 1

def simple_x2(x):
    return x + 1

x0 = bisect(simple_x1, -10, 10, 1.e-10)
print x0

x0 = bisect(simple_x2, -10, 10, 1.e-10)
print x0


