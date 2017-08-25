
class Walls():
    def __init__(self,length,width):
        self.length  = length
        self.width   = width
        Wall = [['X' for x in range(length)] for y in range(width)]
        self.Wall =  Wall
