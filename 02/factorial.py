
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

#print factorial(6) # 720

def print_factorial(n):
    nnn = [n]
    print "factorial(%d)" % (n)
    r = factorial1(nnn)
    print "=", r

def factorial1(nnn):

    n = nnn[-1]
    if n == 1:
        return 1

    ss = " * ".join(map(str, nnn))
    nnn.append(n-1)
    print "= %s * factorial(%d)" % (ss, n-1)
    n2 = factorial1(nnn)
    print "= %s * %d" % (ss, n2)
    return n*n2

print_factorial(6) # 720


def print_factorial(n):
    nnn = [n]
    print "factorial(%d)" % (n)
    r = fact_iter1(1, 1, n)
    print "=", r

def fact_iter1(product, counter, max_count):

    print "= fact_iter(%d, %d, %d)" % (product, counter, max_count)
    if counter > max_count:
        return product
    else:
        return fact_iter1((counter*product), (counter+1), max_count)

def fatorial(n):
    return fact_iter(1, 1, n)

def fact_iter(product, counter, max_count):
    if counter > max_count:
        return product
    else:
        return fact_iter((counter*product), (counter+1), max_count)

print factorial(6) # 720
print print_factorial(6) # 720
