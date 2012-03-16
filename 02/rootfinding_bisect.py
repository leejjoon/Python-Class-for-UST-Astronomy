
def bisect(f, a, b, tol):
    """ given a function f, find a root between a and b with tolerence of tol"""
    f_a = f(a)
    f_b = f(b)

    if f_a * f_b > 0:
        return None

    while True:
        c = 0.5*(a + b)
        f_c = f(c)

        if abs(f_c) < tol:
            return c
            
        if f_a * f_c < 0: # root between a and b
            b = c
        else:
            a = c
            
def simple_x(x):
    return x - 1

x0 = bisect(simple_x, -10, 10, 1.e-10)
print x0
