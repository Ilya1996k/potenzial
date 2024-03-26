def el(a, index, value):
    a = list(a)
    a[index] = value
    return tuple(a)


def append(a, value):
    a= list(a)
    a = a + [value]
    return tuple(a)


def start(a, value):
    a = list(a)
    a = [value] + a
    return tuple(a)
