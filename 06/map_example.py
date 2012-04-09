
a = range(5)

import operator

reduce(operator.concat, [[3], [4], [5]])


def f_with_def(x):
    return x+2

f_with_lambda = lambda x: x+2

f_with_lambda(3) # 5

a = map(lambda x: x*x, [1, 2, 3, 4, 5])
b = map(lambda x, y: x+y, [1, 2, 3], [3, 4, 5])

import operator
b = map(operator.add, [1, 2, 3], [3, 4, 5])

from operator import itemgetter
c = filter(itemgetter(0), [(True, "a"), (False, "b"), (True, "c")])


import re
p = re.compile(r"^source\d\s")
ss = filter(p.match, open("test.txt"))

def check_substring(a, b):
    return a in b

# result = []
# for l in open("test.txt"):
#     if "source1" in l
# c = filter(itemgetter(0), [(True, "a"), (False, "b"), (True, "c")])

#from itertools import
from functools import partial


#    results.append()

#ss = filter(p.match, open("test.txt"))

if 1:
    from operator import methodcaller
    s3 = filter(lambda (name, ra, dec): dec > 0,
                map(lambda l0: (l0[0], float(l0[1]), float(l0[2])),
                    map(methodcaller("split"),
                        filter(None,
                               map(lambda l:l.strip().split("#")[0],
                                   open("test.txt"))))))


if 1:

    from operator import methodcaller
    takeout_comments = lambda stream: \
                       filter(None, map(lambda l:l.strip().split("#")[0],
                                        stream))

    split_items = lambda stream: map(methodcaller("split"), stream)

    ra_dec_to_float = lambda stream: \
                      map(lambda l0: (l0[0], float(l0[1]), float(l0[2])),
                          stream)

    filter_positive_dec = lambda stream: \
                          filter(lambda (name, ra, dec): dec > 0,
                                 stream)

    s3 = filter_positive_dec( \
           ra_dec_to_float( \
             split_items( \
               takeout_comments(open("test.txt")))))


if 1:
    takeout_comments = lambda stream: \
                       (l.strip().split("#")[0] for l in stream)
    filter_empty_lines = lambda stream: \
                         (l0.split() for l0 in stream if l0)
    ra_dec_to_float = lambda stream: \
                      ((l1[0], float(l1[1]), float(l1[2])) for l1 in stream)
    filter_neg_dec = lambda stream: \
                      (l2 for l2 in stream if l2[2] > 0)

    s3 = list(filter_neg_dec( \
                ra_dec_to_float( \
                  filter_empty_lines( \
                    takeout_comments(open("test.txt"))))))
