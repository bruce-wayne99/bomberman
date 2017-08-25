from time import time
from person import Person
class Bomb(Person):
    def __init__(self,radius,timelimit,type,lefttop_x,lefttop_y,det):
        Person.__init__(self,type,lefttop_x,lefttop_y)
        self.radius = radius
        self.timelimit = timelimit
        self.det = det
    def CheckIfTime(self,grid,detonation,enemycount,bombercount,score):
        if detonation == self.timelimit:
            return self.Explode(grid,enemycount,bombercount,score)
        else:
            return [grid,enemycount,bombercount,[],[],score]
    def Explode(self,grid,enemycount,bombercount,score):
        x = self.get_lefttop_x()
        y = self.get_lefttop_y()
        Box = self.Collide(grid,x,y,enemycount,bombercount,1,[],[],score)
        Box = self.Collide(Box[0],x,y+4,Box[1],Box[2],0,Box[3],Box[4],Box[5])
        Box = self.Collide(Box[0],x,y-4,Box[1],Box[2],0,Box[3],Box[4],Box[5])
        Box = self.Collide(Box[0],x+2,y,Box[1],Box[2],0,Box[3],Box[4],Box[5])
        Box = self.Collide(Box[0],x-2,y,Box[1],Box[2],0,Box[3],Box[4],Box[5])
        return Box;
    def Collide(self,grid,x,y,enemycount,bombercount,collide_type,array,enemies_died,score):
        if grid[x][y] !='X':
            if grid[x][y]=='/':
                score+=20
            if collide_type==1 and self.CheckIfBomberman(grid,x,y):
                bombercount-=1
            if grid[x][y] == 'B' and collide_type==0:
                bombercount-=1
            if grid[x][y] == 'E' and collide_type==0:
                enemycount-=1
                enemies_died.append([x,y])
            grid[x][y] = 'e'
            grid[x][y+1] = 'e'
            grid[x][y+2] = 'e'
            grid[x][y+3] = 'e'
            grid[x+1][y] = 'e'
            grid[x+1][y+1] = 'e'
            grid[x+1][y+2] = 'e'
            grid[x+1][y+3] = 'e'
            array.append([x,y])
        return [grid,enemycount,bombercount,array,enemies_died,score]
    def ClearGridAfterBlast(self,grid,array):
        for ele in array:
            x = ele[0]
            y = ele[1]
            grid[x][y] = ' '
            grid[x][y+1] = ' '
            grid[x][y+2] = ' '
            grid[x][y+3] = ' '
            grid[x+1][y] = ' '
            grid[x+1][y+1] = ' '
            grid[x+1][y+2] = ' '
            grid[x+1][y+3] = ' '
        return grid
