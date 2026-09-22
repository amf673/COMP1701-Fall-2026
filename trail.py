# COMP 1701 Trail difficulty

KM_TO_METERS = 1_000


def km2m( d_km:float) -> float:
    """ Return the distance in m, given d_km in
        kilometers
    """
    d_m = d_km * KM_TO_METERS
    return d_m
    

def main() -> None:
    
    # input
    distance_km = float( input( "Enter the trail distance (e.g. 4.5): "))
    elevation_m = int( input( "Enter the trail elevation (e.g. 450): "))
    
    # processing 
    distance_m = km2m( distance_km)
    
    slope = elevation_m / distance_m 
    slope_percentage = slope * 100
    
    #output 
    output_str = f"The trail is {distance_km} km long, goes up {elevation_m} m and has slope {slope_percentage:.0f}%."
    print( output_str)
    
main() 