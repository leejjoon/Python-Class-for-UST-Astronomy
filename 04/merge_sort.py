if 1:
    def mergesort(l):
        if len(l) < 2:
            return l
        middle = len(l) / 2
        left = mergesort(l[:middle])
        right = mergesort(l[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        left_top = left[0]
        right_top = right[0]

        if left_top <= right_top:
            result.append(left_top)
            del left[0]
        else:
            result.append(right_top)
            del right[0]

    if left: result.extend(left)
    if right: result.extend(right)

    return result

unsorted_list = [2, 5, 12, 62, 743, 6, 20]
sorted_list = mergesort(unsorted_list)
