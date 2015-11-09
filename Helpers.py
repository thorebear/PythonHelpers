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
    pivot = _list[random.randint(0, len(_list) - 1)]
    a = [x for x in _list if x < pivot]
    b = [x for x in _list if x > pivot]
    mid = [x for x in _list if x == pivot]
    return quicksort(a) + mid + quicksort(b)

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

def select_menu_item(items):
    """
    Create a selectable menu for the items listed in 'items'
    """
    print "Select one of the following:"
    _count = 1
    for i in items:
        print "[" + str(_count) + "]" + " " + str(i)
        _count = _count + 1

    _in = raw_input("Input 1 to " + str(len(items)) + "  ")
    try:
        _in_int = int(_in)
        if 1 <= _in_int <= len(items):
            return items[_in_int-1]
        else:
            select_menu_item(items)
    except ValueError:
        print "Please input integer"
        select_menu_item(items)
        