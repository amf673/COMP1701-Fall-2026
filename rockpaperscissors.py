#
# Play a game of Rock-Paper-Scissors
#
# Alan
# COMP 1701

import random

ROCK      = "R"
PAPER     = "P"
SCISSORS  = "S"

def comp_choice() -> str:
    """ return the computers choice. Randomly
    pick ROCK, or PAPER or SCISSORS """

    pick = random.randint( 1,3)
    if pick == 1:
        choice = ROCK
    elif pick == 2:
        choice = PAPER
    else:
        choice = SCISSORS
    
    return choice


def rps( player1:str, player2:str) -> bool:
    """ Return True if player 1 wins, False for a loss or Tie
    """
    
    cond1 = ( player1 == ROCK)     and ( player2 == SCISSORS) # rock crushes scissors 
    cond2 = ( player1 == SCISSORS) and ( player2 == PAPER)    # scissors cuts paper
    cond3 = ( player1 == PAPER)    and ( player2 == ROCK)     # paper covers rock
    win =   ( cond1 or cond2 or cond3)
    
    return win

def pp( p1:str, p2:str, res:bool)->None:
    """ convenience function """
    print( f"{p1:^8} {p2:^8} {res}")

def testing():
    print( "PLAYER  COMPUTER  RESULT")
    print( "------------------------")
    pp( ROCK, PAPER, rps( ROCK, PAPER))
    pp( ROCK, SCISSORS, rps( ROCK,SCISSORS))
    pp( ROCK, ROCK, rps( ROCK,ROCK))
    pp( PAPER, PAPER, rps( PAPER,PAPER))
    pp( PAPER, SCISSORS, rps( PAPER,SCISSORS))
    pp( PAPER, ROCK, rps( PAPER,ROCK))
    pp( SCISSORS, PAPER, rps( SCISSORS,PAPER))
    pp( SCISSORS, SCISSORS, rps( SCISSORS,SCISSORS))
    pp( SCISSORS, ROCK, rps( SCISSORS,ROCK))
    

def testing2():
    print( comp_choice()) 

# testing2()


def main():
    # Play the game
    my_choice = input( "Enter R or P or S: ")
    c_choice = comp_choice()
    
    if (my_choice == c_choice):
        print( "Tie Game")
    elif ( rps( my_choice, c_choice)):
        print( "I WIN!")
    else:
        print( "Computer WINS!")
               
# main()
testing()
