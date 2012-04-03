def mergesort(l):
    if len(l) < 2:
        return l
    middle = len(l) / 2
    left = mergesort(l[:middle])
    right = mergesort(l[middle:])
    return merge(left, right)

def merge(left, right):
    result = []

    iter_left = iter(left)
    iter_right = iter(right)

    heap = [(iter_left.next(), iter_left),
            (iter_right.next(), iter_right)]

    try:
        while True:
            v, itr = min(heap)
            heap.remove((v, itr))
            result.append(v)
            heap.append((itr.next(), itr))
    except StopIteration:
        pass

    v, itr = heap[0]
    result.append(v)
    result.extend(itr)

    return result

unsorted_list = [2, 5, 12, 62, 743, 6, 20]

#print mergesort(unsorted_list)
assert mergesort(unsorted_list) == sorted(unsorted_list)
