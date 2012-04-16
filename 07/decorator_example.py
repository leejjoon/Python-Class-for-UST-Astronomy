if 1:
    from contextlib import contextmanager

    @contextmanager
    def my_file(name):
        print "file %s is opened" % name
        f = open(name)
        yield f
        f.close()
        print "file %s is closed" % name

    with my_file("test.txt") as f:
        print "123"
