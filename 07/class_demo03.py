class MyList2(list):
    instance_counts = 0

    def __init__(self, *kl):
        super(MyList2, self).__init__(*kl)
        self.increase_instance_counts()

    def increase_instance_counts(cls):
        cls.instance_counts += 1

    increase_instance_counts = classmethod(increase_instance_counts)

    def print_instance_counts(cls):
        print cls.instance_counts

    print_instance_counts = classmethod(print_instance_counts)

    def print_name():
        print "MyList2"

    print_name = staticmethod(print_name)


a1 = MyList2([1, 2, 3])
a2 = MyList2([1, 2, 3])
MyList2.print_instance_counts() # 2
MyList2.print_name()
