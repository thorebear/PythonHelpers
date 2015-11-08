import random

def letter_range(start, end, step=1):
    """
    Returns the range of letters between 'start'
    and 'end' in the ascii table
    """
    return [chr(x) for x in range(ord(start), ord(end), step)]

def scan_exl(op, e, _list):
    """
    Exclusive scan with:
    - Associative operator op
    - Neutral element e
    - List _list
    """
    if len(_list) == 0:
        return _list
    result = [e]
    for x in _list[:-1]:
        result.append(op(result[-1], x))
    return result

def scan_inc(op, e, _list):
    """
    Inclusive scan with
    - Associative operator op
    - Neutral element e
    - List _list
    """
    if len(_list) == 0:
        return _list
    result = [op(e, _list[0])]
    for x in _list[1:]:
        result.append(op(result[-1], x))
    return result

def quicksort(_list):
    """
    Quicksort of list _list
    """
    if len(_list) <= 1:
        return _list
    r = random.randint(0, len(_list) - 1)
    pivot = _list.pop(r)
    a = []
    b = []
    for v in _list:
        if v <= pivot:
            a.append(v)
        else:
            if v > pivot:
                b.append(v)
    a = quicksort(a)
    b = quicksort(b)
    return a + [pivot] + b  