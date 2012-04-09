if 1:

    available_shapes = ["circle", "ellipse", "box"]

    def ds9_region(self):
        pass


if 1:
    def ds9_region(self, shape, x, y, *kl, **kwargs):
        if not shape in self.available_shapes:
            raise ValueError("shape name %s is not supported")

        self.shape = shape
        self.x, self.y = x, y
        self._kl = kl
        self._kwargs = kwargs

if 1:
    class SomeClass:

        some_attribute = ["circle", "ellipse", "box"]

        def some_function():
            pass

    #print SomeClass.some_attribute
    #print SomeClass.some_function() # raise an TypeError

    class SomeClass2:

        some_attribute = ["circle", "ellipse", "box"]

        def print_some_attribute(self):
            print self.some_attribute

        def set_instance_attribute(self, value):
            self.instance_attribute = value

        def print_instance_attribute(self):
            print self.instance_attribute


    a_instance = SomeClass2() # create an instance of SomeClass2
    print a_instance.some_attribute
    SomeClass2.print_some_attribute(a_instance)
    a_instance.print_some_attribute()
    #print SomeClass2.some_function() # raise an TypeError
    #a_instance.print_instance_attribute() # AttributeError
    a_instance.set_instance_attribute("test")
    a_instance.print_instance_attribute()
