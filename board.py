from random import random
from walls import Walls
from bricks import Bricks
from enemy import Enemy
from colorama import Fore

class Board(Walls,Bricks):
    def __init__(self,rows,columns,brickslimit,length,width):
        Walls.__init__(self,rows,columns)
        Bricks.__init__(self,brickslimit,length,width)
        self.enemies = []

    def CreateEmptyBoard(self):
        Grid = [[' ' for x in range(self.columns)] for y in range(self.rows)]
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
