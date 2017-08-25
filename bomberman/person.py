class Person():
    def __init__(self,type,lefttop_x,lefttop_y):
        self.type = type
        self._lefttop_x = lefttop_x
        self._lefttop_y = lefttop_y
    def get_lefttop_x(self):
        return self._lefttop_x
    def get_lefttop_y(self):
        return self._lefttop_y
    def get_persontype(self):
        return self.type
    def set_lefttop_x(self,val):
        self._lefttop_x = val
    def set_lefttop_y(self,val):
        self._lefttop_y = val
    def set_detonation(self,val):
        self._det = val
    def get_detonation(self):
        return self._det
    def PopulateGridWithPerson(self,grid):
        if self.type==1:
            x = self.get_lefttop_x()
            y = self.get_lefttop_y()
            grid[x][y]='B'
            grid[x][y+1]='B'
            grid[x][y+2]='B'
            grid[x][y+3]='B'
            grid[x+1][y]='B'
            grid[x+1][y+1]='B'
            grid[x+1][y+2]='B'
            grid[x+1][y+3]='B'
        elif self.type==2:
            x = self.get_lefttop_x()
            y = self.get_lefttop_y()
            grid[x][y]='E'
            grid[x][y+1]='E'
            grid[x][y+2]='E'
            grid[x][y+3]='E'
            grid[x+1][y]='E'
            grid[x+1][y+1]='E'
            grid[x+1][y+2]='E'
            grid[x+1][y+3]='E'
        return grid
    def ClearGridOfPerson(self,grid,move_type):
        if move_type==0 or move_type == 3:
            x = self.get_lefttop_x()
            y = self.get_lefttop_y()
            grid[x][y]=' '
            grid[x][y+1]=' '
            grid[x][y+2]=' '
            grid[x][y+3]=' '
            grid[x+1][y]=' '
            grid[x+1][y+1]=' '
            grid[x+1][y+2]=' '
            grid[x+1][y+3]=' '
        if move_type==1:
            x = self.get_lefttop_x()
            y = self.get_lefttop_y()
            grid[x][y]=str(self.get_detonation())
            grid[x][y+1]=str(self.get_detonation())
            grid[x][y+2]=str(self.get_detonation())
            grid[x][y+3]=str(self.get_detonation())
            grid[x+1][y]=str(self.get_detonation())
            grid[x+1][y+1]=str(self.get_detonation())
            grid[x+1][y+2]=str(self.get_detonation())
            grid[x+1][y+3]=str(self.get_detonation())
        return grid
    def Move(self,direction,grid,move_type):
        if direction=='a':
            if self.type == 1 and grid[self.get_lefttop_x()][self.get_lefttop_y()-3]=='E' and grid[self.get_lefttop_x()+1][self.get_lefttop_y()-3]=='E':
                return self.BomberManSuicide('a',grid,move_type)
            if grid[self.get_lefttop_x()][self.get_lefttop_y()-1]==' ' or move_type == 3:
                grid = self.ClearGridOfPerson(grid,move_type)
                self.set_lefttop_x(self.get_lefttop_x())
                self.set_lefttop_y(self.get_lefttop_y()-4)
                return self.PopulateGridWithPerson(grid)
            else:
                return grid
        if direction=='d':
            if self.type == 1 and grid[self.get_lefttop_x()][self.get_lefttop_y()+5]=='E' and grid[self.get_lefttop_x()+1][self.get_lefttop_y()+5]=='E':
                return self.BomberManSuicide('d',grid,move_type)
            if grid[self.get_lefttop_x()][self.get_lefttop_y()+4]==' ' or move_type == 3:
                grid = self.ClearGridOfPerson(grid,move_type)
                self.set_lefttop_x(self.get_lefttop_x())
                self.set_lefttop_y(self.get_lefttop_y()+4)
                return self.PopulateGridWithPerson(grid)
            else:
                return grid
        if direction=='w':
            if self.type == 1 and grid[self.get_lefttop_x()-2][self.get_lefttop_y()+1]=='E' and grid[self.get_lefttop_x()-1][self.get_lefttop_y()+1]=='E':
                return self.BomberManSuicide('w',grid,move_type)
            if grid[self.get_lefttop_x()-1][self.get_lefttop_y()]==' ' or move_type == 3:
                grid = self.ClearGridOfPerson(grid,move_type)
                self.set_lefttop_x(self.get_lefttop_x()-2)
                self.set_lefttop_y(self.get_lefttop_y())
                return self.PopulateGridWithPerson(grid)
            else:
                return grid
        if direction=='s':
            if self.type == 1 and grid[self.get_lefttop_x()+2][self.get_lefttop_y()+1]=='E' and grid[self.get_lefttop_x()+3][self.get_lefttop_y()+1]=='E':
                return self.BomberManSuicide('s',grid,move_type)
            if grid[self.get_lefttop_x()+2][self.get_lefttop_y()]==' ' or move_type == 3:
                grid = self.ClearGridOfPerson(grid,move_type)
                self.set_lefttop_x(self.get_lefttop_x()+2)
                self.set_lefttop_y(self.get_lefttop_y())
                return self.PopulateGridWithPerson(grid)
            else:
                return grid
        return grid
    def CheckIfBomberman(self,grid,lefttop_x,lefttop_y):
        x = lefttop_x
        y = lefttop_y
        if grid[x][y]=='B':
            return True
        else:
            return False
