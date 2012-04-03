def reverse(data):
    for index in xrange(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print char

