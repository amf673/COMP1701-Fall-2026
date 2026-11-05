#
#
# Some loop examples ...
# 

def counted_loop( n:int) -> None:
    """ A sample counted loop """
    
    i = 0 # intialize the loop control variable (LCV)
    
    while (i < n): # the start of the loop. Loop continues while the
                   # condition is True
        # Body of the loop
        print( i)
        i = i + 1 # update the loop control variable
    
    print( "Loop is complete:")
    
    
def sentinel_loop() -> None:
    """ a sample sentinel loop that runs
    as long as the user enters a Y"""
    
    resp = input( "Do you want to continue?: ") # resp is the LCV
    
    while resp == "y":   # continue with loop as long as the user enter 'y' 
        # body of the loop 
        print( "in the loop...")
        
        resp = input( "Do you want to continue?: ")
        
    print( 'Loop is complete')
    

def sentinel_loop_accum() -> int:
    """ a sentinel loop with an accumulator. Returns the
    sum of a list of postive numbers """
    
    num = int( input( "Enter a number, 0 to quit:  ")) # resp is the LCV
    sum = 0 
    while num > 0:   # continue with loop as long as the user enters positive numbers  
        # body of the loop 
        sum = sum + num
        num = int( input( "Enter a number, 0 to quit:  ")) # resp is the LCV

        
    print( 'Loop is complete')
    return sum

    
def main():
    counted_loop( 10)
    sentinel_loop()
    print( sentinel_loop_accum()) 

main()