from person import Person
import random


class Enemy(Person):
    def __init__(self, lefttop_x, lefttop_y, type):
        Person.__init__(self, type, lefttop_x, lefttop_y)

    ''' The RandomMove function takes a the topmost x,y coordinates of The
        enemy and checks all the grids and takes the possible positions
        into an array and selects a random move
    '''

    def RandomMove(self, grid):
        x = self.get_lefttop_x()
        y = self.get_lefttop_y()
        possible_pos = []
        ''' The possible positions are a empty grid or a grid with a bomberman
            therefore it checks if either it is empty or contains a bomberman
        '''
        if ((grid[x][y - 1] == ' ' or self.CheckIfBomberman(grid, x,
                                                            y - 1)) and (x != 2 or y != 8)):
            possible_pos.append('a')

        if grid[x][y + 4] == ' ' or self.CheckIfBomberman(grid, x, y + 4):
            possible_pos.append('d')

        if ((grid[x - 1][y] == ' ' or self.CheckIfBomberman(grid,
                                                            x - 1, y)) and (x != 4 or y != 4)):
            possible_pos.append('w')

        if grid[x + 2][y] == ' ' or self.CheckIfBomberman(grid, x + 2, y):
            possible_pos.append('s')

        if len(possible_pos) == 0:
            return 'no move'

        move_pos = random.choice(possible_pos)

        ''' Finally the return value is an array of the containing the character
            direction to move and another integer which is 3 if a bomberman is
            going to get killed or 0 if bomberman is not going to get killed
        '''
        if move_pos == 'a' and self.CheckIfBomberman(grid, x, y - 4):
            return [move_pos, 3]

        if move_pos == 'd' and self.CheckIfBomberman(grid, x, y + 4):
            return [move_pos, 3]

        if move_pos == 'w' and self.CheckIfBomberman(grid, x - 2, y):
            return [move_pos, 3]

        if move_pos == 's' and self.CheckIfBomberman(grid, x + 2, y):
            return [move_pos, 3]

        return [move_pos, 0]
