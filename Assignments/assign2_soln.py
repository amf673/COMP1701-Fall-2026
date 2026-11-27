# 
# 
# COMP 1701 Fall 2026 
# 
# Assignment 2 Diagnoses
#
# A. Fedoruk 


import math

ORAL_TEMP_FEVER               = 37.8
UNDERARM_TEMP_FEVER           = 37.2
HEART_RATE_VARIABILITY_CUTOFF = 50
CORTISOL_CUTOFF               = 25.0
ORAL                          = 'o'
UNDERARM                      = 'u'

# diagnoses 
FLU                           = "flu"
HEALTHY                       = "healthy"
STRESS                        = "stress"
INFECTION                     = "infection"


def temperature_is_fever( temperature: float, site: str) -> bool:
    """
    determines whether a given temperature and test site represents fever
    parameters:
       temperature: the recorded temperature in °C
       site: either "oral" or "underarm"
    returns: True if an oral temp is at least 37.8°, or an underarm temp is at least 37.2°
    """
   
    return ( temperature >= ORAL_TEMP_FEVER and site == ORAL) or \
        ( temperature >= UNDERARM_TEMP_FEVER and site == UNDERARM)


def is_y( resp:str) -> bool:
    """ Returns True is resp is a y or Y """
    
    return resp == 'y' or resp == 'Y'


def has_low_HRV( interval1:float, interval2:float, interval3:float) -> bool:
    """
    True if these intervals represent a HRV less than 50 ms
    """
    
    diff1 = interval1 - interval2
    diff2 = interval2 - interval3
    avg_sq_diff = ( diff1 ** 2 + diff2 ** 2) / 2
    hrv = math.sqrt( avg_sq_diff)
    
    return (hrv < HEART_RATE_VARIABILITY_CUTOFF)


def has_high_cortisol( cortisol:float) -> bool:
    """
    asks the user to enter their cortisol level
    returns True if the level is above 25.0
    """

    return (cortisol > CORTISOL_CUTOFF)


def num_healthy( client_results:list) -> int:
    """ return the number of HEALTHY diagnoses in the list """
    
    i = 0
    count = 0
    while i < len( client_results):
        if client_results[i] == HEALTHY:
            count = count + 1
        i = i + 1
        
    return count
        

def main() -> None:
    """
    Assignment 2 Prompt for new client's until no more clients! 
    """
   
    # create two parallel lists, one with client names, the other with
    # cliet diagnoses. Not strictly needed for this, but fun.
    
    client_names = []
    client_results = []
   
    # use a sentinel loop to read client names until blank entered. 
    client = input( "Enter the client's name. <Return> When no more clients: ")
    while client != "":
       
        # assume healthy 
        diagnosis = HEALTHY
        
        temperature = float( input( "Enter your temperature (°C): "))
        site = input( "Was the temperature measured Orally (O) or Underarm (U)? (enter O or U): ").lower()
      
        if temperature_is_fever( temperature, site):
            
            nausea = input( "Are you experiencing nausea? (enter y or n): ")
            
            if is_y( nausea):
                diagnosis = FLU
            else:
                diagnosis = INFECTION
                
        else:
            # HRV 
            print( 'Please enter 3 heartbeat intervals in ms...')
            int_a = float( input('Enter first interval: '))
            int_b = float( input('Enter second interval: '))
            int_c = float( input('Enter third interval: '))
         
            if has_low_HRV( int_a, int_b, int_c):
                
                cortisol = float( input( 'Enter cortisol level in mcg/dL: '))
                
                if has_high_cortisol( cortisol):
                    diagnosis = STRESS
                    
        # add the client name and diagnosis to the lists. 
        client_names.append( client)
        client_results.append( diagnosis)
        
        print( f"\nClient: {client} Diagnosis: {diagnosis}\n")
        
        client = input( "Enter the client's name. <Return> When no more clients: ")
      
    print( "\nSummary")
    print( f"\tClients: {len( client_names)}")
    print( f"\tHealthy: {num_healthy( client_results)}")
   

main()
