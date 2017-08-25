from random import random

class Bricks():
    def __init__(self,brickslimit,length,width):
        self.brickslimit = brickslimit
        self.length = length
        self.width = width

    def PopulateBoardWithBricks(self,Grid):
        count = 0
        for i in range(2,self.rows-2):
            if i%2==0:
                for j in range(4,self.columns-4):
                    if j%4==0 and Grid[i][j]!='X':
                        if random() > 0.7 and count<self.brickslimit and (i!=2 or j!=4) and (i!=2 or j!=8) and (i!=4 or j!=4):
                            Grid[i][j]='/'
                            Grid[i][j+1]='/'
                            Grid[i][j+2]='/'
                            Grid[i][j+3]='/'
                            Grid[i+1][j]='/'
                            Grid[i+1][j+1]='/'
                            Grid[i+1][j+2]='/'
                            Grid[i+1][j+3]='/'
                            count = count + 1
        return Grid
