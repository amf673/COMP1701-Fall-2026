#
# mt2 practise
CABIN_LIMIT = 8
CHECKED_LIMIT = 23 

def within_limit( weights: list, bag_type: str) -> list:
    """ q12) """
    bags = [] 
    i = 0
    while i < len( weights):
        bag_check = False
        if bag_type == "cabin" and weights[i] <= CABIN_LIMIT:
            bag_check = True
        
        if bag_type == "checked" and weights[i] <= CHECKED_LIMIT:
            bag_check = True 
            
        i = i + 1
        bags.append(bag_check)
    return bags
    

def main():
    # 9) 
    mountains = [] 
    
    mountain_name = input( "Enter a mountain name: ")
    while mountain_name.strip() != "":
        mountains.append( mountain_name)
        mountain_name = input( "Enter a mountain name: ")
    print( mountains)
    
    # 10)
    elevations = []
    i = 0
    while i < len( mountains):
        elevation = int( input( f"Enter elevation of {mountains[i]} in meters"))
        elevations.append(elevation)
        i = i + 1
    
    print( mountains, elevations)
    
    # 11) 
    i = 0
    print( f"{'Mountain':^20}{'Elevation':^20}")
    print( "-" * 40)
    while i < len( mountains):
        print( f"{mountains[i]:20}{elevations[i]:20}")
        i = i + 1
        
    print( "-" * 40)

def testing():
    
    print( within_limit( [8, 9, 7, 4, 30], "checked")) 

# main()
testing()
