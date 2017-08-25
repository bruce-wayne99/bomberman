from random import random
from walls import Walls
from bricks import Bricks
from enemy import Enemy
from colorama import Fore

class Board(Walls,Bricks):
    def __init__(self,rows,columns,brickslimit,length,width):
        self.rows = rows
        self.columns = columns
        self._brickslimit = brickslimit
        Walls.__init__(self,length,width)
        Bricks.__init__(self,length,width)
        self.enemies = []
    def GetBrickslimit(self):
        return self._brickslimit

    def SetBrickslimit(self,val):
        self._brickslimit = val

    def CreateEmptyBoard(self):
        Grid = [[' ' for x in range(self.columns)] for y in range(self.rows)]
        return Grid
    def PopulateBoardWithElement(self,x,y,Grid,temp):
        Grid[x][y]=temp[0][0]
        Grid[x][y+1]=temp[0][1]
        Grid[x][y+2]=temp[0][2]
        Grid[x][y+3]=temp[0][3]
        Grid[x+1][y]=temp[1][0]
        Grid[x+1][y+1]=temp[1][1]
        Grid[x+1][y+2]=temp[1][2]
        Grid[x+1][y+3]=temp[1][3]
        return Grid
    def PopulateBoardWithWalls(self,Grid):
        x = 0
        y = 0
        while y<self.columns:
            wall = Walls(4,2)
            temp = wall.Wall
            Grid = self.PopulateBoardWithElement(x,y,Grid,temp)
            y+=4
        x = self.rows-2
        y = 0
        while y<self.columns:
            wall = Walls(4,2)
            temp = wall.Wall
            Grid = self.PopulateBoardWithElement(x,y,Grid,temp)
            y+=4
        x = 4
        y = 0
        while x<self.rows-2:
            while y<self.columns:
                wall = Walls(4,2)
                temp = wall.Wall
                Grid = self.PopulateBoardWithElement(x,y,Grid,temp)
                y+=8
            x+=4
            y=0
        x = 0
        y = 0
        while x<self.rows:
            wall = Walls(4,2)
            temp = wall.Wall
            Grid = self.PopulateBoardWithElement(x,y,Grid,temp)
            x+=2
        x = 0
        y = self.columns-4
        while x<self.rows:
            wall = Walls(4,2)
            temp = wall.Wall
            Grid = self.PopulateBoardWithElement(x,y,Grid,temp)
            x+=2
        return Grid

    def PopulateBoardWithBricks(self,Grid):
        count = 0
        for i in range(2,self.rows-2):
            if i%2==0:
                for j in range(4,self.columns-4):
                    if j%4==0 and Grid[i][j]!='X':
                        if random() > 0.7 and count<self.GetBrickslimit() and (i!=2 or j!=4) and (i!=2 or j!=8) and (i!=4 or j!=4):
                            brick = Bricks(4,2)
                            temp = brick.Brick
                            Grid = self.PopulateBoardWithElement(i,j,Grid,temp)
                            count = count + 1
        return Grid

    def PopulateBoardWithEnemies(self,grid,max_enemies):
        count = 0
        for i in range(2,self.rows-2):
            if i%2==0:
                for j in range(4,self.columns-4):
                    if j%4==0 and grid[i][j]==' ':
                        if random()>0.9 and count < max_enemies and (i!=2 or j!=4) and (i!=2 or j!=8) and (i!=4 or j!=4):
                            enemy = Enemy(i,j,2)
                            self.enemies.append(enemy)
                            grid = enemy.PopulateGridWithPerson(grid)
                            count = count+1
        return grid

    def RemoveEnemyFromList(self,x,y):
        for i in range(len(self.enemies)):
            if self.enemies[i].get_lefttop_x()== x and self.enemies[i].get_lefttop_y()==y:
                self.enemies.remove(self.enemies[i])
                break

    def PrintBoard(self,grid):
        for i in grid:
            for j in i:
                if j=='B':
                    print(Fore.CYAN+j,end="")
                elif j=='X':
                    print(Fore.YELLOW+j,end="")
                elif j=='/':
                    print(Fore.MAGENTA+j,end="")
                elif j=='E':
                    print(Fore.RED+j,end="")
                elif j=='e':
                    print(Fore.GREEN+j,end="")
                else:
                    print(Fore.WHITE+j,end="")
            print("")
