# 
# lists.py
#
# use list indexing and slicing and the list concatenation operator, +.


def head( alist:list) -> list:
    """ Return a singleton list consisting of the first element of alist.
        If alist is empty return the empty list.  """
    return alist[0:1] 

def tail( alist:list) -> list:
    """ Return a list consisting of the tail of alist. That is, everything 
        except the first element. If there is only one element or alist is empty
        return the empty list.  """
    return alist[1:]

def append( alist:list, item) -> list:
    """ Append item to the end of alist and return the new list """
    return alist + [item]


def add( alist:list, item) -> list:
    """ Add item at the start of alist and return the new list   """
    return [item] + alist

def insert( alist:list, item, i:int) -> list:
    """ insert item into the list at position i.  if i is out of range, 
    insert item at the end of the list. Return the new list.  
    """
    return alist[:i] + [item] + alist[i:]


def sum( alist:list) -> float:
    """ Return the sum of all of the items in alist. If there are non-numeric 
    items in the list, an error will occur.  """
    
    i = 0
    accumulator = 0.0
    while i < len(alist):
        accumulator = accumulator + alist[i]
        i = i + 1
    return accumulator


def avg( alist:list) -> float:
    """ Return the average of all of the items in alist.  If there are 
    non-numeric items in the list, an error will occur.  If there are 
    no items in the list, return 0.0 """
    sum_of_list = sum( alist) # make use of sum above. 
    n = len( alist)
    if n != 0: # protect against divide by 0
        average = sum_of_list / n
    else:
        average = 0.0
    return average

def max_min( alist:list, max:bool) -> float:
    """ Return the max if max is True, min if it is False in alist. If there are no items in the 
    list, return None """
    maxormin = None
    if len(alist) > 0:
        maxormin = alist[0]
        i = 1
        while (i < len( alist)):
            if (alist[i] > maxormin and max) or (alist[i] < maxormin and not max): 
                maxormin = alist[i]
            i = i + 1
    return maxormin 

def max( alist:list) -> float:
    """ Return the maximum item in alist. If there are no items in the 
    list, return None """
    return max_min( alist, True)


def min( alist:list) -> float:
    """ Return the minimum item in alist. If there are no items in the 
    list, return None """
    return max_min( alist, False) 

def loc( alist:list, item) -> int:
    """ Return the index of item in alist. If item is not present 
    return -1. """
    i = 0
    found = -1
    while (i < len(alist)):
        if alist[i] == item:
            found = i
        i = i + 1
    return found

def delete_ind( alist:list, i:int) -> list: 
    """ Return a list with the item at index i deleted. If it exists.
    """
    return alist[:i] + alist[i+1:]


def delete( alist:list, item):
    """ delete the item from alist, if it exists. Return the item if was in
    the list, None otherwise """
    
    i = loc( alist, item)
    if i != -1: 
        return delete_ind( alist, i)
    else:
        return None

def count( alist:list, item)-> int:
    """ Return a count of how many times item occurs in alist """
    n = 0
    i = 0 
    while i < len( alist):
        if alist[i] == item:
            n = n + 1
        i = i + 1
    
    return n

def print_list( alist:list) -> str:
    prn_str = "["
    for i in range( 0, len( alist), 1):
        if i == len( alist) - 1: 
            prn_str = prn_str + f"{alist[i]}"
        else:
            prn_str = prn_str + f"{alist[i]}, "
    prn_str = prn_str + "]"
    return prn_str

def main():
    a = ["blue", "green", "green", "red", "blue", "yellow"]
    print( "GREEN COUNT = ", count( a, "green"))
    print( "CYAN COUNT = ", count( a, "cyan"))
    print( "EMPTY LIST COUNT = ", count( [], "cyan"))

print( "Module __name__ = ", __name__)

if __name__ == "__main__":
    main()

    
