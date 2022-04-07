# Name: Ow Yong Chee Seng   
# Student number: 61164992

"""
    This program implements one variety of the snake 
    game (https://en.wikipedia.org/wiki/Snake_(video_game_genre))
"""

from asyncio import Task
import threading
import queue        #the thread-safe queue from Python standard library

from tkinter import Tk, Canvas, Button
import random, time

class Gui():
    """
        This class takes care of the game's graphic user interface (gui)
        creation and termination.
    """
    def __init__(self, queue, game):
        """        
            The initializer instantiates the main window and 
            creates the starting icons for the snake and the prey,
            and displays the initial gamer score.
        """
        #some GUI constants
        scoreTextXLocation = 60
        scoreTextYLocation = 15
        textColour = "white"
        #instantiate and create gui
        self.root = Tk()
        self.canvas = Canvas(self.root, width = WINDOW_WIDTH, 
            height = WINDOW_HEIGHT, bg = BACKGROUND_COLOUR)
        self.canvas.pack()
        #create starting game icons for snake and the prey
        self.snakeIcon = self.canvas.create_line(
            (0, 0), (0,0), fill=ICON_COLOUR, width=SNAKE_ICON_WIDTH)
        #create prey icon 
        self.preyIcon = self.canvas.create_rectangle(
            0, 0, 0, 0, fill=ICON_COLOUR, outline=ICON_COLOUR)
        #display starting score of 0
        self.score = self.canvas.create_text(
            scoreTextXLocation, scoreTextYLocation, fill=textColour, 
            text='Your Score: 0', font=("Helvetica","11","bold"))
        #binding the arrow keys to be able to control the snake
        for key in ("Left", "Right", "Up", "Down"):
            self.root.bind(f"<Key-{key}>", game.whenAnArrowKeyIsPressed)

    def gameOver(self):
        """
            This method is used at the end to display a
            game over button.
        """
        gameOverButton = Button(self.canvas, text="Game Over!", 
            height = 3, width = 10, font=("Helvetica","14","bold"), 
            command=self.root.destroy)
        self.canvas.create_window(200, 100, anchor="nw", window=gameOverButton)
    

class QueueHandler():
    """
        This class implements the queue handler for the game.
    """
    def __init__(self, queue, gui):
        self.queue = queue #initialise the queue
        self.gui = gui
        self.queueHandler() #use this function to operate
    
    def queueHandler(self):
        '''
            This method handles the queue by constantly retrieving
            tasks from it and accordingly taking the corresponding
            action.
            A task could be: game_over, move, prey, score.
            Each item in the queue is a dictionary whose key is
            the task type (for example, "move") and its value is
            the corresponding task value.
            If the queue.empty exception happens, it schedules 
            to call itself after a short delay.
        '''
        try:
            while True:
                task = self.queue.get_nowait()
                if "game_over" in task: 
                    gui.gameOver() #call gameover function 
                elif "move" in task:
                    points = [x for point in task["move"] for x in point]
                    gui.canvas.coords(gui.snakeIcon, *points) #change canvas coordinates of snake icon 
                elif "prey" in task: #put a new prey on screen
                    gui.canvas.coords(gui.preyIcon, *task["prey"])
                elif "score" in task:
                    gui.canvas.itemconfigure( #display score on screen 
                        gui.score, text=f"Your Score: {task['score']}")
                self.queue.task_done()
        except queue.Empty:
            gui.root.after(100, self.queueHandler)


class Game():
    '''
        This class implements most of the game functionalities.
    '''
    def __init__(self, queue):
        """
           This initializer sets the initial snake coordinate list, movement
           direction, and arranges for the first prey to be created.
        """
        self.queue = queue
        self.score = 0
        #starting length and location of the snake
        #note that it is a list of tuples, each being an
        # (x, y) tuple. Initially its size is 5 tuples.       
        self.snakeCoordinates = [(495, 55), (485, 55), (475, 55),
                                 (465, 55), (455, 55)] 
        #initial direction of the snake
        self.direction = "Left"
        self.gameNotOver = True
        #### mycode
        self.preyXLocation = 0
        self.preyYLocation = 0
        #### mycode
        self.createNewPrey()

        
        
    def superloop(self) -> None:
        """
            This method implements a main loop
            of the game. It constantly generates "move" 
            tasks to cause the constant movement of the snake.
            Use the SPEED constant to set how often the move tasks
            are generated.
        """
        SPEED = 0.15     #speed of snake updates (sec)
        while self.gameNotOver:
            #complete the method implementation below
            time.sleep(SPEED) #update every 0.15 seconds
            self.move()
            # pass #remove this line from your implemenation

    def whenAnArrowKeyIsPressed(self, e) -> None:
        """ 
            This method is bound to the arrow keys
            and is called when one of those is clicked.
            It sets the movement direction based on 
            the key that was pressed by the gamer.
            Use as is.
        """
        currentDirection = self.direction
        #ignore invalid keys
        if (currentDirection == "Left" and e.keysym == "Right" or 
            currentDirection == "Right" and e.keysym == "Left" or
            currentDirection == "Up" and e.keysym == "Down" or
            currentDirection == "Down" and e.keysym == "Up"):
            return
        self.direction = e.keysym

    def move(self) -> None:
        """ 
            This method implements what is needed to be done
            for the movement of the snake.
            It generates a new snake coordinate. 
            If based on this new movement, the prey has been 
            captured, it adds a task to the queue for the updated
            score and also creates a new prey.
            It also calls a corresponding method to check if 
            the game should be over. 
            The snake coordinates list (representing its length 
            and position) should be correctly updated.
        """
        NewSnakeCoordinates = self.calculateNewCoordinates()
        #complete the method implementation below

        #check if gameover 
        print(NewSnakeCoordinates)
        self.isGameOver(NewSnakeCoordinates)

        #check if capture prey
        print(f"check prey location : {self.preyXLocation, self.preyYLocation}")
        #have buffer of 5 pixels because aiming to get one random pixel is hard (especially when we move in multiples of 10 )
        if NewSnakeCoordinates[0] >= self.preyXLocation -5 and NewSnakeCoordinates[0] <= self.preyXLocation +5 \
            and NewSnakeCoordinates[1] >= self.preyYLocation-5 and NewSnakeCoordinates[1] <= self.preyYLocation +5:
            #update score
            self.score+=1
            gameQueue.put({"score":self.score})
            # add one block to the snake 
            self.snakeCoordinates.append(NewSnakeCoordinates) #add the new snake coorcinates 
            #put new prey 
            self.createNewPrey()
        else : 
            #do not add one block to snake (remove one then add one head so length is the same) 
            self.snakeCoordinates.pop(0) #move accordingly 
            self.snakeCoordinates.append(NewSnakeCoordinates) #add the new snake coorcinates 
        gameQueue.put({"move":self.snakeCoordinates}) #move the snake if all is well 

    def calculateNewCoordinates(self) -> tuple:
        """
            This method calculates and returns the new 
            coordinates to be added to the snake
            coordinates list based on the movement
            direction and the current coordinate of 
            head of the snake.
            It is used by the move() method.    
        """
        lastX, lastY= self.snakeCoordinates[-1]
        #complete the method implementation below
        if self.direction == "Left":
            # print("left")
            lastX -= 10
        elif self.direction == "Right":
            # print("right")
            lastX +=10
        elif self.direction == "Up":
            # print("up")
            lastY-=10
        else : 
            # print("down")
            lastY+=10        
        return lastX, lastY

    def isGameOver(self, snakeCoordinates) -> None:
        """
            This method checks if the game is over by 
            checking if now the snake has passed any wall
            or if it has bit itself.
            If that is the case, it updates the gameNotOver 
            field and also adds a "game_over" task to the queue. 
        """
        x, y = snakeCoordinates
        #complete the method implementation below
        #out of bound check
        if x> WINDOW_WIDTH or x< 0 or y > WINDOW_HEIGHT or y <0 : 
            self.gameNotOver= False
            gameQueue.put("game_over")
        #self bite check
        for i in range(len(self.snakeCoordinates)):
            if x == self.snakeCoordinates[i][0] and y == self.snakeCoordinates[i][1] : 
                self.gameNotOver= False
                gameQueue.put("game_over")
    def createNewPrey(self) -> None:
        """ 
            This methods randomly picks an x and a y as the coordinate 
            of the new prey and uses that to calculate the 
            coordinates (x - 5, y - 5, x + 5, y + 5). 
            It then adds a "prey" task to the queue with the calculated
            rectangle coordinates as its value. This is used by the 
            queue handler to represent the new prey.                    
            To make playing the game easier, set the x and y to be THRESHOLD
            away from the walls. 
        """
        THRESHOLD = 15   #sets how close prey can be to borders
        #complete the method implementation below
        self.preyXLocation = random.randint(THRESHOLD, WINDOW_WIDTH-THRESHOLD)
        self.preyYLocation = random.randint(THRESHOLD, WINDOW_HEIGHT-THRESHOLD)
        preyCoordinates = [self.preyXLocation-5, self.preyYLocation-5, self.preyXLocation+5, self.preyYLocation+5]
        #add prey task to queue
        gameQueue.put({"prey": preyCoordinates})

if __name__ == "__main__":
    #some constants for our GUI
    WINDOW_WIDTH = 500           
    WINDOW_HEIGHT = 300 
    SNAKE_ICON_WIDTH = 15
    
    BACKGROUND_COLOUR = "green" 
    ICON_COLOUR = "yellow" 

    gameQueue = queue.Queue()     #instantiate a queue object using python's queue class

    game = Game(gameQueue)        #instantiate the game object

    gui = Gui(gameQueue, game)    #instantiate the game user interface
    
    QueueHandler(gameQueue, gui)  #instantiate our queue handler    
    
    #start a thread with the main loop of the game
    threading.Thread(target = game.superloop, daemon=True).start()

    #start the GUI's own event loop
    gui.root.mainloop()
    