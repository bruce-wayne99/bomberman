from time import time
from person import Person


class Bomb(Person):

    def __init__(self, radius, timelimit, type, lefttop_x, lefttop_y, det):
        Person.__init__(self, type, lefttop_x, lefttop_y)
        self._radius = radius            # Indicates the radius of the blast
        self._timelimit = timelimit      # Indicates the detonation time
        self._det = det         # Used for displaying the counter on the bomb

    def get_timelimit(self):
        return self._timelimit

    def set_timelimit(self, val):
        self._timelimit = val

    # CheckIfTime is used to check if the detonation time has occurred or not

    def CheckIfTime(self, grid, detonation, enemycount, bombercount, score):
        if detonation == self.get_timelimit():
            return self.Explode(grid, enemycount, bombercount, score)
        else:
            return [grid, enemycount, bombercount, [], [], score]

    ''' If the detonation time has occurred it calls Explode which calls the
        which checks whether to collide with the grid or not and keeps track
        of all the enemies died in the process and also if the bomberman
        is dead
    '''

    def Explode(self, grid, enemycount, bombercount, score):
        x = self.get_lefttop_x()
        y = self.get_lefttop_y()

        ''' When we send the grid in which the bomber is present
            we take collide_type = 1
        '''
        Box = self.Collide(grid, x, y, enemycount, bombercount, 1, [],
                           [], score)
        Box = self.Collide(Box[0], x, y + 4, Box[1], Box[2], 0, Box[3],
                           Box[4], Box[5])
        Box = self.Collide(Box[0], x, y - 4, Box[1], Box[2], 0, Box[3],
                           Box[4], Box[5])
        Box = self.Collide(Box[0], x + 2, y, Box[1], Box[2], 0, Box[3],
                           Box[4], Box[5])
        Box = self.Collide(Box[0], x - 2, y, Box[1], Box[2], 0, Box[3],
                           Box[4], Box[5])
        return Box

    def Collide(self, grid, x, y, enemycount, bombercount, collide_type,
                array, enemies_died, score):

        if grid[x][y] != 'X':
            if grid[x][y] == '/':
                score += 20
            if collide_type == 1 and self.CheckIfBomberman(grid, x, y):
                bombercount -= 1
            if grid[x][y] == 'B' and collide_type == 0:
                bombercount -= 1
            if grid[x][y] == 'E' and collide_type == 0:
                enemycount -= 1
                ''' Appends the coordinates of enemies died to later
                    remove from the enemy array
                '''
                enemies_died.append([x, y])
            grid[x][y] = 'e'
            grid[x][y + 1] = 'e'
            grid[x][y + 2] = 'e'
            grid[x][y + 3] = 'e'
            grid[x + 1][y] = 'e'
            grid[x + 1][y + 1] = 'e'
            grid[x + 1][y + 2] = 'e'
            grid[x + 1][y + 3] = 'e'
            array.append([x, y])  # Appends the positions to be cleared

        return [grid, enemycount, bombercount, array, enemies_died, score]

    # Used to clear the grid after the blast has occured

    def ClearGridAfterBlast(self, grid, array):

        for ele in array:
            x = ele[0]
            y = ele[1]
            grid[x][y] = ' '
            grid[x][y + 1] = ' '
            grid[x][y + 2] = ' '
            grid[x][y + 3] = ' '
            grid[x + 1][y] = ' '
            grid[x + 1][y + 1] = ' '
            grid[x + 1][y + 2] = ' '
            grid[x + 1][y + 3] = ' '
        return grid
