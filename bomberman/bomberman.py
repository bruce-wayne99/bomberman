from person import Person
from bomb import Bomb
class Bomberman(Person):
    def __init__(self,lefttop_x,lefttop_y,type):
        Person.__init__(self,type,lefttop_x,lefttop_y)
        self._det = 1
        self.activeBombs = []
    def PlotBomb(self,grid,radius,timelimit,det):
        newBomb = Bomb(radius,timelimit,3,self.get_lefttop_x(),self.get_lefttop_y(),det)
        self.activeBombs.append(newBomb)
        return grid
    def BomberManSuicide(self,direction,grid,move_type):
        grid = self.ClearGridOfPerson(grid,move_type)
        return [grid,0]
