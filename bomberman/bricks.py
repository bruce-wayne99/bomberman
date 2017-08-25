
class Bricks():
    def __init__(self,length,width):
        self.length = length
        self.width = width
        Brick = [['/' for x in range(length)] for y in range(width)]
        self.Brick =  Brick
