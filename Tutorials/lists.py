
# lists.py
#
# 
# Write the body of these functions that operate on lists. You can only 
# use list indexing and slicing and the list concatenation operator, +.


def head( alist:list) -> list:
    """ Return a singleton list with the first element of alist If alist 
        is empty return the empty list.  """
    pass

def tail( alist:list) -> list:
    """ Return a list consisting of the tail of alist. That is, everything 
        except the first element. If there is only one element, the tail
        is the first element.  If alist is empty return the empty list.  """
    pass

def append( alist:list, item) -> None:
    """ Append item to the end of alist.  """
    pass

def add( alist:list, item) -> None:
    """ Add item at the start of alist.  """
    pass

def insert( alist:list, item, i:int) -> None:
    """ insert item into the list at position i.  if i is out of range, 
    insert item at the end of the list. 
    """
    pass

def sum( alist:list) -> float:
    """ Return the sum of all of the items in alist. If there are non-numeric 
    items in the list, an error will occur.  """
    pass

def avg( alist:list) -> float:
    """ Return the average of all of the items in alist.  If there are 
    non-numeric items in the list, an error will occur.  If there are 
    no items in the list, return 0.0 """
    pass

def max( alist:list) -> float:
    """ Return the maximum item in alist. If there are no items in the 
    list, return None """
    pass


def min( alist:list) -> float:
    """ Return the minimum item in alist. If there are no items in the 
    list, return None """
    pass

def loc( alist:list, item) -> int:
    """ Return the index of item in alist. If item is not present 
    return -1. """

def delete_ind( alist:list, i:int):
    """ Delete the item at index i, if it exists.
    return the item if it was in the list, None otherwise.
    """
    pass


def delete( alist:list, item):
    """ delete the item from alist, if it exists. Return the item if was in
    the list, None otherwise """
    pass
