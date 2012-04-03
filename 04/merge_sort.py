def mergesort(l):
    if len(l) < 2:
        return l
    middle = len(l) / 2
    left = mergesort(l[:middle])
    right = mergesort(l[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        left_top = left[i]
        right_top = right[j]

        if left_top <= right_top:
            result.append(left_top)
            i += 1
        else:
            result.append(right_top)
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


unsorted_list = [2, 5, 12, 62, 743, 6, 20]

assert mergesort(unsorted_list) == sorted(unsorted_list)
