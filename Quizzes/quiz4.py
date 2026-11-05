#
# Quiz 4
#
# Some notes:
#
# In both cases the function requirement is to `return` the string. Printing it is not the same.
# In both cases the input to the function comes from the parameter (wind_speed or slope).
# Both use an if else-if structure to have mutually exclusive options. Note in the wind speed function
# that when the interpreter is running the line marked "here", we know that wind_speed is more than 33.
# 
# 
# Complete the following function. It takes a wind speed in knots 
# and returns a string with the Marine Weather Warning as follows:
# 
#   - less than 18 knots is Calm
#   - 18 to 33 knots is a Small Craft Warning
#   - 34 to 47 knots is a Gale Warning
#   - More than 47 knots is a Storm Warning

def marine_weather( wind_speed: int) -> str:
    """ Return the marine weather warning given the wind speed in knots"""
    
    if wind_speed < 18:
        warning = "Calm"
    elif wind_speed <= 33:
        warning = "Small Craft Warning"
    elif wind_speed <= 47: # here
        warning = "Gale Warning"
    else
        warning = "Storm Warning"
        
    return warning 

#
# 
# Complete the following function. It takes the slope of a hiking trail 
# and returns a string with the expected difficulty of the trail as follows: 

#
#  - less than 5% slope is Easy
#  - 5\% to 10% slope is a Moderate
#  - 11\% to 25% is Hard
#  - More than 25% slope is Extreme

def hiking_difficulty( slope: int) -> str:
    """ Return the difficuly of a trail given its percent slope. """
    
    if slope < 5:
        difficulty = "Easy"
    elif slope <= 10:
        difficulty = "Moderate"
    elif slope <= 25:
        difficulty = "Hard"
    else:
        difficuly = "Extreme"
    
    return difficulty



