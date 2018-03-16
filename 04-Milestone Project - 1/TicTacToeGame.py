from os import system
import random

def drawBoard(board):
     # This function prints out the board that it was passed.
     # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('   |   |')

def inputPlayerLetter():
     # Lets the player type which letter they want to be.
     # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    letter = ''
    while True:
        print('Player1: Do you want to be X or O?')
        letter = input().upper()
    # the first element in the list is the player’s letter, the second is the computer's letter.
        if letter == 'X':
            return {'Player 1':'X', 'Player 2':'O'}
        elif letter =='O':
            return {'Player 1':'O', 'Player 2':'X'}
        
def choose_turn():
    if random.randint(0,1)==0:
        return 'Player 1'
    else:
        return 'Player 2'

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move].strip()!='X' and board[move].strip()!='O'

def getPlayerMove(board,player):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        move = input(f'{player}: What is your next move? (1-9)')
    return int(move)

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board,letter,move):
    board[move]=' '+letter+' '
    system('clear')
    return drawBoard(board)
    
def isWinner(board,letter):
    return (
        (board[7].strip()==board[8].strip()==board[9].strip()==letter) or #Row 1
        (board[4].strip()==board[5].strip()==board[6].strip()==letter) or #Row 2
        (board[1].strip()==board[2].strip()==board[3].strip()==letter) or #Row 3 
        (board[7].strip()==board[4].strip()==board[1].strip()==letter) or #Column 1
        (board[8].strip()==board[5].strip()==board[2].strip()==letter) or #Column 2
        (board[9].strip()==board[6].strip()==board[3].strip()==letter) or #Column 3
        (board[7].strip()==board[5].strip()==board[3].strip()==letter) or #Diagonal
        (board[1].strip()==board[5].strip()==board[9].strip()==letter) #Diagonal
    )
def isBoardFilled(board):
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    print("It's a draw")
    return True

def tic_tac_toe():
    system('clear')
    print("Welcome to Tic Tac Toe!")
    playerLetter=inputPlayerLetter()
    turn = choose_turn()
    board=['[0]','[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]']
    drawBoard(board)
    print(f'{turn} goes first')
    while not isBoardFilled(board):
            makeMove(board, playerLetter[turn], getPlayerMove(board, turn))
            if(isWinner(board, playerLetter[turn])):
                print(f"{turn} wins!!!")
                break
            elif isBoardFilled(board):
                break;
            elif turn=='Player 1':
                turn = 'Player 2'
            else:
                turn = 'Player 1'
        
def __main__():
    tic_tac_toe()
    while playAgain():
        tic_tac_toe()

__main__()
    
    