from board import Board
from bomberman import Bomberman
from person import Person
from enemy import Enemy
from bomb import Bomb
from random import random
a = Board(42,84,50,2,4)
b = a.CreateEmptyBoard()
b = a.PopulateBoardWithWalls(b)
b = a.PopulateBoardWithBricks(b)
man = Bomberman(2,4,1)
b = man.PopulateGridWithPerson(b)
en = Enemy(2,8,2)
b = en.PopulateGridWithPerson(b)
