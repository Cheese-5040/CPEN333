# student name: Ow Yong Chee Seng
# student number: 61164992
from importlib.abc import TraversableResources
import random

class TicTacToe:
    def __init__(self): # Use as is
        """ initializes data fields (board and played) 
            and prints the banner messages 
            and prints the initial board on the screen
        """
        self.board = [' '] * 9 # A list of 9 strings, one for each cell, 
                               # will contain ' ' or 'X' or 'O'
        self.played = set()    # Set (of cell num) already played: to keep track of the played cells 
        print("Welcome to Tic-Tac-Toe!")
        print("You play X (first move) and computer plays O.")
        print("Computer plays randomly, not strategically.")
        self.printBoard()

    def printBoard(self) -> None:
        """ prints the board on the screen based on the values in the self.board data field """
        printBoard = ""
        for i in range(3):
            #printing the board alone, and the last right cell does not need a divider
            for j in range(3):
                printBoard+= (f" {self.board[3*i + j]} |")if j <2 else  (f" {self.board[3*i + j]} ") 
            #adding space between the board and the numbered board
            printBoard+= (f"\t")

            #filling in the numbered board
            for k in range(3):
                #the last right cell does not need a divider
                printBoard += (f" {3*i + k} |") if k <2 else  (f" {3*i + k} ") 
            #adding lines at the bottom of each row except last row
            printBoard += (f"\n --+---+---\t --+---+---\n")if i <2 else  (f"") 
        
        print(printBoard)

    def playerNextMove(self) -> None:
        """ prompts the player for a valid cell number; 
            error checks that the input is a valid cell number; 
            and prints the info and the updated self.board;
        """
        #use while statement to get repeated request until the correct answer is given 
        while True:
            try:
                cellNum = int(input(f"Next move for X (state a valid cell num)"))
            #if the input is not an integer
            except ValueError: 
                print("Must be an integer")
                continue
            #if input is invalid, which is either out of bounds or not filled 
            if cellNum < 0 or cellNum>8 or self.board[cellNum] != " ":
                print("Must enter a valid cell number")
                continue
            else:
                #the cellNum is correctly parsed, with no errors
                break
        

        print(f"You choose cell {cellNum}")
        self.board[cellNum] = "X"
        self.printBoard()

    def computerNextMove(self) -> None:
        """ computer randomly chooses a valid cell, 
            and prints the info and the updated self.board 
        """
        compCell = random.randint(0, 7) #pick rand number from 0-8
        #checling for a valid, empty cell within bounds of the board
        while compCell < 0 or compCell>8 or self.board[compCell] != " ":
            compCell = random.randint(0, 7)
        print(f"Computer chose cell {compCell}")
        self.board[compCell] = "O"
        self.printBoard()


    def hasWon(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won, False otherwise """
        #win conditions: 
        #check for verticals or diagonals
        for i in range(3): 
            if self.board[i]==self.board[i+3]==self.board[i+6]==who:
                return True
        #check for horizontals
        for i in range(0, 9, 3):
            if self.board[i]==self.board[i+1] == self.board[i+2]==who:
                return True
        #diagonals, 0,4,8, 2,4,6
        if self.board[0] == self.board[4] == self.board[8]==who or self.board[2] == self.board[4] ==self.board[6]==who :
            return True
        return False
    def terminate(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
            it also prints the final messages:
                 "You won! Thanks for playing." or 
                 "You lost! Thanks for playing." or 
                 "A draw! Thanks for playing."  
        """
        empty = False
        for i in range(9):
            if self.board[i] == " ":
                # print("is empty")
                empty = True

        #without board completely filled 
        if self.hasWon(who) :
            #player won 
            if (who == "X"):
                print("You won! Thanks for playing." )
                return True
            #computer won 
            elif (who == "O"):
                print("You lost! Thanks for playing.")
                return True
        #board filled but no one won or lost yet
        elif self.hasWon("O")==self.hasWon("X")==False and empty == False:
            print("A draw! Thanks for playing.")  
            return True
        else:
            #this means not empty, and no one won yet, so contibue the game 
            return False

if __name__ == "__main__":  # Use as is
    ttt = TicTacToe()  # initialize a game
    while True:
        ttt.playerNextMove()            # X starts first
        if(ttt.terminate('X')): break   # if X won or a draw, print message and terminate
        ttt.computerNextMove()          # computer plays O
        if(ttt.terminate('O')): break   # if O won or a draw, print message and terminate