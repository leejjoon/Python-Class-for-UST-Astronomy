def mergesort(l):
    if len(l) == 1:
        yield l[0]
    elif len(l) > 0:
        middle = len(l) / 2
        iter_left = mergesort(l[:middle])
        iter_right = mergesort(l[middle:])
        for v in merge(iter_left, iter_right): yield v


def merge(iter_left, iter_right):
    # This must be a generator
    pass

unsorted_list = [2, 5, 12, 62, 743, 6, 20]

assert list(mergesort(unsorted_list)) == sorted(unsorted_list)
