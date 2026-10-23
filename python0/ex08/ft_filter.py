
def ft_filter(function, iterable):
    """Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true."""

    for i in iterable:
        if function is None:
            if i:
                yield i
        elif function(i):
            yield i
