if 0:
    for i in [2, 1, 0, -1, -2]:
        try:
            a = 2/i
        except ZeroDivisionError:
            break
        else:
            print i, a
        finally:
            print "finally with %d" % i
            raise ValueError("")

if 1:
    def a():
        1/0

    def b():
        try:
            a()
        except ValueError:
            pass

    def c():
        try:
            b()
        except ZeroDivisionError:
            print "I'm here!"

    c()


