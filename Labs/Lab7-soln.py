# 
# 
# L7 - More Loops 
# COMP 1701 Fall 2026
# 
# A. Fedoruk
# 
# Includes solutions with while loops and for loops



def enter_str( prompt:str)->str:
    """ Prompt user with `prompt' and return a non-empty string."""

    resp = input( prompt).strip()
    while resp == "":
        resp = input( f"String must be non-empty. {prompt}").strip()

    return resp.strip()


def enter_int( prompt:str) -> int:
    """ Prompt for a integer """

    resp = enter_str( prompt)
    num = int( resp)
    while num < 0: 
        resp = enter_str( prompt)
        num = int( resp)

    return num


def enter_int_range( prompt:str, low:int, high:int)->int:
    """ Prompt for a int in the given range """

    resp = enter_str( prompt)
    num = int( resp)
    while not(num >= low and num <= high): 
        resp = enter_str( prompt)
        num = int( resp)

    return num


def yorn( prompt:str) -> bool: 
    """ Prompt for the user to enter y or n"""

    resp = input( prompt).strip().lower()
    while not( resp == "y" or resp =="n"):
         resp = input( prompt).strip()

    return resp == "y"
   
   
def count_up( bound:int) -> str:
    """ Count up from 0 to bound and return a string
        using a for loop """

    count_str = ""
    i = 0
    while i <= bound:
        if count_str == "": 
            count_str = "0"
        else:
            count_str = count_str + "," + str( i )
        i = i + 1

    return count_str


def count_up_f( bound:int) -> str:
    """ Count up from 0 to bound and return a string
        using a for loop """

    count_str = ""
    for i in range( 0, bound + 1):
        if count_str == "": 
            count_str = "0"
        else:
            count_str = count_str + "," + str( i)

    return count_str


def count_between( l:int, u:int) -> str:
    """ Return a string of numbers between l and u using a for """

    count_str = ""
    i = l + 1
    while i <= u:
        if count_str == "": 
            count_str = str( i)
        else:
            count_str = count_str + "," + str( i)
        i = i + 1

    return count_str


def count_between_f( l:int, u:int) -> str:
    """ Return a string of numbers between l and u using a for """

    count_str = ""
    for i in range( l + 1, u + 1):
        if count_str == "": 
            count_str = str( i)
        else:
            count_str = count_str + "," + str( i)

    return count_str


def string_between( low:str, high:str) -> str:
    """ Return the characters between low and high """

    l = ord( low)
    h = ord( high)
    result = ""
    i = l + 1
    while i < h:
        if i % 2 == 0:
            result = result + chr( i).upper()
        else:
            result = result + chr( i).lower()
        i = i + 1

    return result


def string_between_f( low:str, high:str) -> str:
    """ Return the characters between low and high using a for """

    l = ord( low)
    h = ord( high)
    result =""
    for i in range( l + 1, h):
        if i % 2 == 0:
            result = result + chr(i).upper()
        else:
            result = result + chr(i).lower()

    return result

    
def main():

    print( enter_str( "Enter a string: "))

    print( enter_int( "Enter a non zero int: "))
    
    print( count_up( 9))
    print( count_up_f( 9))
    
    print( count_between( 3, 8))
    print( count_between_f( 3, 8))
    
    print( string_between( 'f', 'm'))
    print( string_between_f( 'f', 'm')) 


main()


