def mergesort(l):
    if len(l) == 1:
        yield l[0]
    elif len(l) > 0:
        middle = len(l) / 2
        iter_left = mergesort(l[:middle])
        iter_right = mergesort(l[middle:])
        for v in merge(iter_left, iter_right): yield v


def merge(iter_left, iter_right):

    heap = [(iter_left.next(), iter_left),
            (iter_right.next(), iter_right)]

    try:
        while True:
            v, itr = min(heap)
            heap.remove((v, itr))
            yield v
            heap.append((itr.next(), itr))
    except StopIteration:
        pass

    v, itr = heap[0]
    yield v
    for v in itr: yield v


unsorted_list = [2, 5, 12, 62, 743, 6, 20]

#print mergesort(unsorted_list)
assert list(mergesort(unsorted_list)) == sorted(unsorted_list)
