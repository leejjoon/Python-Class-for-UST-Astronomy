class MyList(list):
    def extend(self, iterable, n=1):
        """
        with optional argument of n, extend the list with iterable n times.
        """
        l = list(iterable)
        for i in range(n):
            super(MyList, self).extend(l)



a = MyList([1, 2, 3])
a.append(4)
a.extend([5, 6], n=3)
