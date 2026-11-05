#
# Play a game of Rock-Paper-Scissors
#
# Alan
# COMP 1701

import random

ROCK      = "R"
PAPER     = "P"
SCISSORS  = "S"

WIN       = "Win!"
TIE       = "Tie"
LOSE      = "Lose"

PROMPT    = "Shall we play a game? "


def comp_choice() -> str:
    """
    Return the computers choice.
    Randomly pick ROCK, or PAPER or SCISSORS """

    pick = random.randint( 1, 3)
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
    


def play_game( player1:str, player2:str) -> str:
    """ Play a game of RPS. Return Tie, Win, Lose if player1 ties, wins or loses.
    """
    
    if (player1 == player2):
        game = TIE
    elif ( rps( player1, player2)):
        game = WIN
    else:
        game = LOSE
        
    return game
    
    

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


# def main():
#     # Play the game
#     
#     resp = input( "outside" + PROMPT) # resp is the loop control variable (LCV) 
#     while ( resp == "y"): # loop condition 
#         # body of the loop
#         my_choice = input( "Enter R or P or S: ")
#         c_choice = comp_choice()
#     
#         print( f"I played {my_choice} and the computer played {c_choice}. ")
#         print( f"\tThe result is: { play_game( my_choice, c_choice)}")
#         
#         resp = input( "inside" + PROMPT)
#

def main():
    # Play the game
    
    n = int( input( "how many games? ")) # i is the loop control variable (LCV)
    i = 0
    wins = 0 
    while ( i < n ): # loop condition 
        # body of the loop
        print( "\nGame ", i + 1 )
        my_choice = input( "Enter R or P or S: ")
        c_choice = comp_choice()
        
        result = play_game( my_choice, c_choice)
        if result == WIN:
            wins = wins + 1 
    
        print( f"I played {my_choice} and the computer played {c_choice}. ")
        print( f"\tThe result is: { result}")
        
        i = i + 1 # update the LCV
    
    print( f"I won {wins} times out of {n} games for a win percentage of {wins/n*100}")
        
           
main()
# testing()