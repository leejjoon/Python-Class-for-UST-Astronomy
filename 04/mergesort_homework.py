def mergesort(l):
    """ Given a list l, return a sorted list"""
    if len(l) < 2:
        return l
    middle = len(l) / 2
    left = mergesort(l[:middle])
    right = mergesort(l[middle:])
    return merge(left, right)

def merge(left, right):
    """
    merge two sorted lists left and right into a single sorted list.
    Return the result.
    """
    result =[]
    # merge left and right.
    return result

unsorted_list = [2, 5, 12, 62, 743, 6, 20]

assert mergesort(unsorted_list) == sorted(unsorted_list)
