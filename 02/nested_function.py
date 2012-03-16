from math import exp

def make_gaussian_function(A, x0, sigma):

    def my_gaussian(x):
        r = A*exp(-(x-x0)**2/(2*sigma**2))
        return r
    
    return my_gaussian


gauss = make_gaussian_function(1, 10, 30)

print gauss(10), gauss(10+2.3548*30/2.)
