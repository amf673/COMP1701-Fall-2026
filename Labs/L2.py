# 
# COMP 1701 
# Lab 2
# Al Fedoruk
# Fall 2026

import math

PAPER_THICKNESS = 0.05 # thickness of a typical sheet of paper in mm
MM_PER_METER = 1000


def mm2m( mm:float) -> float:
    """ Return the value or mm millimeters in meters) """
    
    return mm / MM_PER_METER


def main():
    
    # ---------------------------------------------------------------- #
    # Question 1 Compound Interest Calculation 

    # input
    initial_investment = float( input( "Enter the initial value of the investment: "))
    rate = float( input( "Enter the interest rate: "))
    time = float( input( "Enter the number of years to invest: "))

    # processing 
    investment_value = initial_investment * ( 1 + rate)**time

    # output note the line continuation \ 
    print( "An investment of", initial_investment, "at", rate * 100, \
          "% will be worth", round( investment_value, 2), "after", time, "years.")


    # ---------------------------------------------------------------- #
    # Question 2 Paper folding

    # input 
    f = int( input( "Enter the number of folds (>0): "))

    # processing 
    thickness = PAPER_THICKNESS * 2**f

    thickness_meters = mm2m( thickness) 
    
    # output 
    print( "A paper", PAPER_THICKNESS, "mm thick if folded ", f, "times, would be ", thickness, "m thick.")
    
    
    # ---------------------------------------------------------------- #
    # Question 3 Doubling Times 

    r = float( input( "Enter the growth rate in percent: "))

    doubling_time = 70 / r 
    exact_doubling_time = ( math.log(2) / math.log( 1 + ( r / 100)))

    print( "At a growth rate of ", r, "doubling occurs in approximately", \
           round( doubling_time, 2), "and exactly ", round( exact_doubling_time,2))
    print("The difference is ", exact_doubling_time - doubling_time)

main()


