class Walls():
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
    def PopulateBoardWithWalls(self,Grid):
        for x in range(self.columns):
            Grid[0][x]='X'
            Grid[1][x]='X'
            Grid[self.rows-1][x]='X'
            Grid[self.rows-2][x]='X'
        for x in range(self.rows):
            Grid[x][0]='X'
            Grid[x][1]='X'
            Grid[x][2]='X'
            Grid[x][3]='X'
            Grid[x][self.columns-1]='X'
            Grid[x][self.columns-2]='X'
            Grid[x][self.columns-3]='X'
            Grid[x][self.columns-4]='X'
        for x in range(4,self.rows-2):
            if x%4==0 or x%4==1:
                for y in range(4,self.columns-4):
                    if y%8<=3:
                        Grid[x][y]='X'
                    else:
                        Grid[x][y]=' '
            else:
                for y in range(4,self.columns-4):
                    Grid[x][y]=' '
        return Grid
