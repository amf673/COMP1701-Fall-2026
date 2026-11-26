import math
import random
import lists_module as lst

def main():
    
#     print( "This is a main method!!")
#     print( math.sqrt( 2.0))
#     print( random.randint( 0,1000))
#
    print( "Module __name__ = ", __name__)
    
    b = ["fox", "bear", "wolverine", "deer", "deer"]
    print( "BEARS = ", lst.count( b, "bear"))
    
    print( lst.print_list( b))
    
main()
