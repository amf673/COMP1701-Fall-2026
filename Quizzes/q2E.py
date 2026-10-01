
# Quiz 2 E
#

C = 299792458 # speed of light in m/s

def energy( m: float) -> float:
    """ Return the energy in joules given the mass in kg according to Einstein's equation """
    
    return m * C * C
