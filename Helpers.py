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
    mid = [pivot]
    for v in _list:
        if v < pivot:
            a.append(v)
        else:
            if v > pivot:
                b.append(v)
            else: #v == pivot
                mid.append(pivot)
    a = quicksort(a)
    b = quicksort(b)
    return a + mid + b


def mergesort(_list):
    """
    Merge sort on _list
    """
    _len = len(_list)
    if _len <= 1:
        return _list
    mid = _len/2
    (a, b) = (mergesort(_list[:mid]), mergesort(_list[mid:]))
    merged = []
    while len(a) > 0 and len(b) > 0:
        a_v = a[0]
        b_v = b[0]
        if a_v < b_v:
            merged.append(a_v)
            a.pop(0)
        else:
            merged.append(b_v)
            b.pop(0)
    return merged + a + b

    
def randlist(size, _min, _max):
    """
    Generate random list with 'size' random ints between _min and _max
    """
    _list = [0] * size
    return [random.randint(_min, _max) for _ in _list]
    