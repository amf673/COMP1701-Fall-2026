#
# tree.py Calculate the height of a tree 
#
# COMP 1701 
# 

import math

PI = math.pi
M_PER_FOOT = 0.3048
INCHES_PER_FOOT = 12

def radians( angle_deg: float) -> float: 
    """ convert angle_deg to radians """

    return angle_deg * (PI/180)


def feet_to_m( feet: float) -> float:
    """ return the number of meters in the given number of feet """

    return feet * M_PER_FOOT 


def inches_to_m( inches:float) -> float:
    """ Return the number of m in the given number of inches """

    return feet_to_m( inches / INCHES_PER_FOOT)


def height( obs_height: float, dist:float, angle: float) -> float:
    """ Return the height of a tree in meters given the observer's height (obs_height), 
    the distance from the base of the tree (dist) and the angle between the ground and 
    the top of the tree (angle).
    """

    h = dist * math.tan( angle) + obs_height

    return h


def main() -> None:
    
    # inputs 
    distance_m = float( input( "Enter the distance in meters: "))
    angle_deg = float( input( "Enter the angle (degrees) between ground and top of tree: "))
    height_feet = float( input( "Enter the observer's height in feet: "))
    height_inches = float( input( "Enter the observer's height in inches: "))

    # processing 
    obs_height = feet_to_m( height_feet) + inches_to_m( height_inches)
    angle_rad = radians( angle_deg)

    height_tree = height( obs_height, distance_m, angle_rad)

    # output 
    print( f"The height of the tree is {height_tree:.2f} m")

main()

