
class Foo: 
    pass

class Foo2: 
    def __init__(self): #constructor of itself 
        self.x = 1 #attribute x 

f = Foo2()
print(Foo2, f, f.x) #f is instantiation of Foo2, f.x is accessing x of f