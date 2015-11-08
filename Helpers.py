

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
    - List list
    """
    if len(_list) == 0:
        return _list
    result = [e]
    for x in _list[:-1]:
        result.append(op(result[-1], x))
    return result

def scan_inc(oper, neutral, _list):
    """
    Inclusive scan with
    - Associative operator op
    - Neutral element e
    - List list
    """
    if len(_list) == 0:
        return _list
    result = [oper(neutral, _list[0])]
    for x in _list[1:]:
        result.append(oper(result[-1], x))
    return result


        