#print("\n*100")
#import the random module to use to decide which player to go first
import random


#function that can print out a board with the index of the tic tac toe board

def display_board(board):

    print("\n"*100)

    #printing the display
    print("----------")
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("----------")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("----------")
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print("----------")
                    
    
def player_input():
    # setting a marker that is not x or o to return a false  in the while loop
    marker = " "

    #running till the player provides an X or and O
    while marker != "X" and marker!= "O":
        marker = input("Player 1 choose a marker, X or O: ").upper()
        
    # returning a tuple so that we can assign it later on 
    if marker == "X":
        return ('X','O')
    else:
        return("O","X")

def place_marker(board, marker,position):
    # writing a fxn that takes a list(board), marker(i.e X or O) and posistion
    # and place the maker at the position
    board[position] = marker

def win_check(board, mark):
    #checking each instance to see if there is a win
    #horizontal win checks = [1][2][3],[4][5][6],[7][8][9]
    #vertical win checks = [1][4][7],[2][5][8],[3][6][9]
    #diagonal win checks = [1][5][9],[3][5][7]
    return((board[1] ==board[2]==board[3]== mark) or
           (board[4] ==board[5]==board[6]== mark) or
           (board[7] ==board[8]==board[9]== mark) or
           
           (board[1] ==board[4]==board[7]== mark) or
           (board[2] ==board[5]==board[8]== mark) or
           (board[3] ==board[6]==board[9]== mark) or
           
           (board[1] ==board[5]==board[9]== mark) or
           (board[3] ==board[5]==board[7]== mark) 
           
        )

def choose_first():
    # using the random module to decide which player goes first
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"


#fxn to determine if a space is available
def space_check(board,position ):
    return (board[position]==' ')

#write a fxn to check if the board is full?
def space_full(board):
    # check to see if there if free space in the board
    for i in range(1,10):
        if space_check(board,i):
            return False
    #return False if there is free space
    #return True if the board is full
    return True
#fxn that ask for a players position and uses space_check t

def player_choice(board):
    position  = 0

    # check to see if the number is in board else check to see space is filled?
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("choose position: (1-9)"))

    #return the position 

    return position

def replay():
    return input("Do you want to replay?(Enter Yes or No): ").lower().startswith("y")

def play_game():
    return input("Are you ready to play? Enter Yes or no ").lower().startswith("y")






print("Welcome to Tic Tac Toe!")

#write a statment that runs over and over to make use of the 
while True:
    #reset the board
    the_board = [" "] * 10
    
    # assign the player the  marker if player 1 chooses X assign o to player 2 and vice versa
    player1_marker,player2_marker = player_input()
    
    #choose the player turn randomly
    turn = choose_first()
    print(f"{turn} will go first")

    game_on =  play_game()

    while game_on:
        # player 1's turn
        if turn == "Player 1":
            
            #display the board
            
            display_board(the_board)
            
            #  let player select a position to place the marker
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            
            #check to see if the player has won the game esle return player 2
            if win_check(the_board,player1_marker):
                #check to see it the player won
                display_board(the_board)
                print("Congratulations! You have won the game! ")
                #return game_on false to break out of the game
                game_on = False
            else:
                #check to see if the space is full 
                if space_full(the_board):
                    display_board(the_board)
                    print("The game is a draw")
                    break
                else:
                    turn = "Player 2"
        else:
            # player 2's turn
            display_board(the_board)
            
            #  let player select a position to place the marker
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            
            #check to see if the player has won the game esle return player 2
            if win_check(the_board,player2_marker):
                #check to see it the player won
                display_board(the_board)
                print("Player 2 has won!! ")
                #return game_on false to break out of the game
                game_on = False
            else:
                #check to see if the space is full 
                if space_full(the_board):
                    display_board(the_board)
                    print("The game is a draw")
                    break
                else:
                    turn = "Player 1"
        
    if not replay():
        break
