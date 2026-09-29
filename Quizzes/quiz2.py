#
# COMP 1701 Fall 2026
# Quiz 2
# 

def foo( a:int, b:float) ->float:
    """ A function that returns a value! """
    # The values when foo() was called are copied
    # into the parameters (local variables) a and b. 
    # 
    
    # Remember PEMDAS to evaluate this.
    # a % 4 is the remainder. So in the example this evaluates to 2.
    # Pay attention to the types. b is a float so (a+b) will be a
    # float and c will be a float. 
    c = a % 4 * (a + b)

    return c


def main() -> None:
    
    f = input( "Enter a number: ")
    g = input( "Enter another number: ")
    # At this point what are f and g?
    
    print( f, type(f))
    print( g, type(g))
    # f and g are both strings!
    # The values of f and g are passed to the function foo() but
    # int(f) is used to covert f to an int and float(g) is used to convert
    # g to a float. 
    h = foo( int( f), float( g))

    
    print( h, type( h))
    
main()
