def qsort(L):
    if L == []: return []

    pivot = L[0]

    left = qsort([x for x in L[1:] if x < pivot])
    right = qsort([x for x in L[1:] if x >= pivot])

    return left + [pivot] + right


a = [2,4,3,5,6]
assert qsort(a) == sorted(a)

b = "python"
print qsort(b)
