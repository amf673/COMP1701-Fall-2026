#
# Alan Fedoruk 
# COMP 1701 003
# 
# Convert from C to F

def to_F( deg_C:int ) -> float:
    """ Returns the equivalent temp in F given a temp 
    in C """
    deg_F = deg_C * 9 / 5 + 32
    return deg_F


def main() -> None:

    degree_c = int( input( "Enter a temperature in degree C: "))
    
    degree_f = to_F( degree_c)

    print( f"{degree_c} is {degree_f} in Fahrenheit")

main()



