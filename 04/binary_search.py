if 1:
    def bsearch(l, a):
        return bsearch1(l, 0, len(l)-1, a)

    def bsearch1(l, p, q, a):
        if p <= q:
            r = (p+q)/2
            if l[r] == a:
                return r
            elif l[r] < a:
                return bsearch1(l, r+1, q, a)
            else:
                return bsearch1(l, p, r-1, a)


