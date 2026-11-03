# Tutorial exercise. Determine price of a service
# COMP 1701 

BASIC = 9.99
PREMIUM = 12.99
DELUXE = 15.99
STAFF = 4.99


def plan_cost( plan:str, staff:bool) -> float:
    """ return the cost of the plan. This should work however the plan is entered i.e: 
    'BaSiC'
     '  Basic'
    'BASIC'
    if staff is True and the is basic reduce the cost to 4.99. 
    """
    plan_str = plan.strip().upper()
    if plan_str == "BASIC":
        if staff:
            cost = STAFF
        else:
            cost = BASIC
    elif plan_str == "PREMIUM":
        cost = PREMIUM
    elif plan_str == "DELUXE":
        cost = DELUXE
    else:
        cost = 0.0
    
    return cost


def testing():
    print( "BASIC",        plan_cost( "BASIC",False))
    print( "PREMIUM",      plan_cost( "PREMIUM",False))
    print( "DELUXE",        plan_cost( "DeLuXE",False))
    print( "    DeLuXE ",   plan_cost( "    DeLuXE ",False))
    print( "premium     ", plan_cost( "premium     ",False))
    print( "ELITE", plan_cost( "ELITE",False))
    
    print( "BASIC",        plan_cost( "BASIC",True))
    print( "PREMIUM",      plan_cost( "PREMIUM",True))
    print( "DELUXE",        plan_cost( "DeLuXE",True))
    print( "    DeLuXE ",   plan_cost( "    DeLuXE ",True))
    print( "premium     ", plan_cost( "premium     ",True))
    print( "ELITE", plan_cost( "ELITE",True))
    

testing() 
    
    
    
    
