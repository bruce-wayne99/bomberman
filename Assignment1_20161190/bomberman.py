from person import Person
from bomb import Bomb


class Bomberman(Person):
    def __init__(self, lefttop_x, lefttop_y, type):
        Person.__init__(self, type, lefttop_x, lefttop_y)
        self._det = 1  # Bomberman also keeps track of timer on bomb
        self.activeBombs = []  # Holds the active bombs planted

    ''' PlotBomb is used by the bomberman to plot a bomb
        in the board
    '''

    def PlotBomb(self, grid, radius, timelimit, det):
        newBomb = Bomb(radius, timelimit, 3, self.get_lefttop_x(),
                       self.get_lefttop_y(), det)
        self.activeBombs.append(newBomb)
        return grid
    ''' This function is implemented when the bomberman
        wantedly goes and collides with the enemy(kind of suicide)
    '''

    def BomberManSuicide(self, direction, grid, move_type):
        grid = self.ClearGridOfPerson(grid, move_type)
        return [grid, 0]
