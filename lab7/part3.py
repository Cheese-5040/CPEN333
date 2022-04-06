class EventManager:
    def __init__(self):
        print("Event Manager: Let me talk to the folks\n")
    
    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()  #a call message 
        
        self.florist = Florist()
        self.florist.setFlowerRequirements()  #a call message
        
        self.caterer = Caterer()
        self.caterer.setCuisine()  #a call message
        
        self.musician = Musician()
        self.musician.setMusicType()  #a call message

        print("Good news, we are set\n") #a response message

class Hotelier:
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")
    
    def __isAvailable(self):
        print("Is the Hotel free for the event on given day?")
        return True
    
    def bookHotel(self):
        if self.__isAvailable():
            print("Hotel is booked\n")  #a response message


class Florist:
    def __init__(self):
        print("Flower Decorations for the Event? --")
    
    def setFlowerRequirements(self):
        print("Carnations, Roses and Lilies are to be used\n") #a response message


class Caterer:
    def __init__(self):
        print("Food Arrangements for the Event --")
    
    def setCuisine(self):
        print("Chinese & Continental Cuisine will be served\n") #a response message


class Musician:
    def __init__(self):
        print("Musical Arrangements for the Marriage --")
    
    def setMusicType(self):
        print("Jazz and Classical will be played\n")  #a response message
    
class Client:
    def __init__(self):
        print("Client: Whoa! My best friend is getting married!")
    def askEventManager(self):
        print("Client: Let's Contact the Event Manager\n")
        eventManager = EventManager()
        eventManager.arrange()   #a call message
    def __del__(self):
        print("Client: Thanks to Event Manager, all preparations done! Phew!")

client = Client()
client.askEventManager() 