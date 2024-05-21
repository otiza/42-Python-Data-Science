

def ft_filter(lambda_, iterable):
    """
    filter(function or None, iterable) --> filter object
    Return an iterator yielding those
    items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if not callable(lambda_):
        raise TypeError("lambda_ must be callable")
    if not hasattr(iterable, "__iter__"):
        raise TypeError("iterable must be iterable")

    return (item for item in iterable if lambda_(item))
