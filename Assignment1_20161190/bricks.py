''' Brick class takes the length and width of the brick and
    outputs the a brick of the corresponding dimensions in
    a 2-D array
'''


class Bricks():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        Brick = [['/' for x in range(length)] for y in range(width)]
        self.Brick = Brick
