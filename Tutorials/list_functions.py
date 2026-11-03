
def head( alist:list) -> list:
    """ returns the head of the list i.e. a list with just the first element
    of alist. i.e. head( [1, 4, 5, 2]) would return [1]. """
    return alist[0:1]

def tail( alist:list) -> list:
    """ returns the tail of the list i.e. a list that excludes the
    first element of alist. i.e. tail([1, 4, 5, 2]) would return [4, 5, 2] """
    return alist[1:]

def middle( alist:list) -> list:
    """ returns the middle elements of alist.
    i.e. middle([1, 4, 5, 2]) would return [4, 5]"""
    return alist[1:len(alist)-1]

def first( alist:list):
    """ returns the first item in alist. """
    if len(alist) == 0:
        result = None
    else:
        result = alist[0]
    return result

def last( alist:list):
    """ returns the last item in alist. """  
    return alist[len(alist)]
