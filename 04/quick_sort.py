if 1:
    def quicksort(l):
        quicksort1(l, 0, len(l)-1)

    def quicksort1(l, p, r):
        if p < r:
            q = partition(l, p, r)
            quicksort1(l, p, q)
            quicksort1(l, q+1, r)

    def partition(l, p, r):
        x = l[p]
        i, j = p, r
        while True:
            while l[j] > x: j-=1
            while l[i] < x: i+=1
            if i<j:
                l[i], l[j] = l[j], l[i]
                i+=1; j-=1
            else:
                return j

    ll = [1, 4, 3, 4, 7, 4, 9, 7, 4]
    quicksort(ll)

