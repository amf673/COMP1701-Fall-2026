#
#
# Assignment 1 
# COMP 1701 Fall 2026
#
# A. Fedoruk

#
# Things to notice:
#
# - All the input() and print() are in main(). (I made a little helper function pr_result() but that could
#   have been in main(). It was just for convenience.
#
# - All the calculations kept all the decimals. Rounding was only done when I printed it out.
#
# - Each function does one thing! Decomposing a problem into functions is hard and takes experiennce and
#   practise. For this one I tried to create a function for each logical operation. (unit conversions,
#   the two tests. Remember a function is a sub-program. Its input is the parameters and the outout
#   is the return value. 

# CONSTANTS

# Conversion Factors 
M_PER_KM     = 1000
LBS_PER_KG   = 2.20462
SEC_PER_MIN  = 60

# For the Cooper test. Ref: https://en.wikipedia.org/wiki/VO2_max
COOPER          = 504.9
COOPER_DENOM    = 44.73

# For the Rockport test. Ref: https://en.wikipedia.org/wiki/VO2_max
ROCKPORT        = 132.853
ROCKPORT_MF     = 6.3150 
ROCKPORT_WEIGHT = 0.0769
ROCKPORT_AGE    = 0.3877 
ROCKPORT_TIME   = 3.2649
ROCKPORT_HR     = 0.1565

# For the output (when using special characters setting up a constant
# is helpful, I find. 
VO2             = "V\u0307O\u2082"
VO2_UNITS       = "mL/(kg\u1427min)"


def km2m( dist:float) -> float:
    """ return the distance in m given dist in km """

    return dist * M_PER_KM


def kg2lb( w:float) -> float: 
    """ return the weight in pounds given w in kg """
    
    return w * LBS_PER_KG


def dec_min( m:int, s:int) -> float:
    """ return the decimal minutes given the minutes and seconds. 0 < s < 60 """

    return m + (s / SEC_PER_MIN)


def cooper( dist:float) -> float:
    """ Return the VO2 max using the Cooper test. Ref: https://en.wikipedia.org/wiki/VO2_max

        - dist is the distance (in km) covered while runing for 12 minutes
        
    """
    
    return ( km2m( dist) - COOPER) / COOPER_DENOM


def rockport( bw:float, age:int, t:float, hr: int, mf:int) -> float:
    """ Return the VO2 max using the Rockport formula Ref: https://en.wikipedia.org/wiki/VO2_max
        
        - bw is the body weight in lbs 
        - age is the age in years 
        - t is the decimal minutes of the time taken to walk 1 mile 
        - hr is the heart rate in bpm at the end of the walk 
        - mf is 0 if the person is female and 1 if the person is male.
        
    """
    
    return ROCKPORT - (ROCKPORT_WEIGHT * bw) - (ROCKPORT_AGE * age) - \
        (ROCKPORT_TIME * t) - (ROCKPORT_HR * hr) + ( mf * ROCKPORT_MF) 


def pr_result( person:str, test:str, vo2_max:float) -> None:
    """ A helper function. Since I print the same thing twice I wrote
        a function for convenience. Notice that I do the rounding here
        and keep all the decimals for the calculations. 
    """
    
    print( f"\n{VO2} Max for {person} is {vo2_max:.2f} {VO2_UNITS} using the {test} test.\n")


def main() -> None:
    
    print( "\nCooper Test\n")

    person = input( "Enter the person's name: ")
    distance = float( input( "Enter the distance, in km, in 12 minutes of running: (e.g 2.4) "))

    vo2_max = cooper( distance) 

    pr_result( person, "Cooper", vo2_max)

    print( "Rockport Test")

    person = input( "Enter the person's name: ")
    age = int( input( "Enter the person's age in years: "))
    weight = float( input( "Enter the person's weight in kg: "))
    time_min = int( input( "Enter the walk time minutes: "))
    time_sec = int( input( "Enter the walk time seconds: "))
    heart_rate = int( input( "Enter the heart rate at the end of the walk in bpm: "))
    
    mf = int( input( "Enter 0 if the person is female, 1 if the person is male: "))

    vo2_max = rockport( kg2lb( weight), age, dec_min( time_min, time_sec), heart_rate, mf)

    pr_result( person, "Rockport", vo2_max)


main() 

