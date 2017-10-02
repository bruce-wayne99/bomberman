''' It works same as the Bricks class and returns a 2-D array
    of the corresponding length and width given
'''


class Walls():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        Wall = [['X' for x in range(length)] for y in range(width)]
        self.Wall = Wall
