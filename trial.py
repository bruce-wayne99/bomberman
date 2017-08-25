import os
import sys
import signal
import time
from colorama import Fore
from getch import getch
from random import random
from board import Board
from bomb import Bomb
from person import Person
from bomberman import Bomberman
from enemy import Enemy

## TAKING INPUTS
TIMEOUT = 1
def interrupted(signum, frame):
    return 1
signal.signal(signal.SIGALRM, interrupted)
def input():
    try:
        foo = getch()
        return foo
    except:
        return 0
##ENDED PART

##DECLARATIONS
a = Board(42,84,50,2,4)
b = a.CreateEmptyBoard()
b = a.PopulateBoardWithWalls(b)
b = a.PopulateBoardWithBricks(b)
man = Bomberman(2,4,1)
b = man.PopulateGridWithPerson(b)
max_enemies = 1
b = a.PopulateBoardWithEnemies(b,max_enemies)
enemies = len(a.enemies)
count = 0
detonation = 0
Active = 0
move_type = 0
max_lifes = 2
score = 0
flag = 0
Resetflag = 0
IterationTime = 0
NextInput = time.time()+1
Synchronous = 0
Timer = 200
##END_DECLARATIONS

def ResetGame(grid,man):
    man = Bomberman(2,4,1)
    grid = man.PopulateGridWithPerson(grid)
    return [grid,man]

def CheckToEnd(max_lifes,enemies):
    if max_lifes == -1 or enemies==0:
        a.PrintBoard(b)
        print(Fore.WHITE+"GAME OVER")
        print(Fore.BLUE+"YOUR SCORE: ",Fore.WHITE+str(score))
        sys.exit()

while Timer>=0:
    signal.alarm(TIMEOUT)
    IterationTime = time.time()

    ##PRINT_PART

    print(Fore.RED+"LIFES AVAILABLE : ",Fore.WHITE+str(max_lifes),'\t',Fore.MAGENTA+"YOUR SCORE : ",Fore.WHITE+str(score),'\t',Fore.GREEN+"TIME : ",Fore.WHITE+str(Timer))
    a.PrintBoard(b)

    ##END_PRINT_PART

    ##BOMBPART

    if Active == -1:
        Active = 0
        detonation = 0
        b = man.activeBombs[0].ClearGridAfterBlast(b,Box[3])
        man.activeBombs=[]
        if flag == 1:
            max_lifes-=1
            CheckToEnd(max_lifes,enemies)
            man = Bomberman(2,4,1)
            b = man.PopulateGridWithPerson(b)
            move_type = 0
            flag = 0
    if Synchronous==1:
        Synchronous = 0
        NextInput=time.time()+1
        if Active == 1:
            flag = 0
            detonation +=1
            Box = man.activeBombs[0].CheckIfTime(b,detonation,enemies,1,score)
            b = Box[0]
            score = Box[5]
            if len(Box[3])==0:
                man.activeBombs[0].set_detonation(man.activeBombs[0].get_detonation()-1)
                man.set_detonation(man.get_detonation()-1)
                if move_type!=1:
                    b = man.activeBombs[0].ClearGridOfPerson(b,1)

            if len(Box[3])!=0:
                Active = -1
                if Box[2]==0:
                    flag = 1
                for num in Box[4]:
                    a.RemoveEnemyFromList(num[0],num[1])
                    score+=100
                    enemies-=1
        CheckToEnd(max_lifes,enemies)
    ##ENDBOMBPART

    ##INPUTPART
    Synchronous = 0
    Resetflag = 0
    s = input()
    if s=='q':
        print(Fore.RED+"YOU QUIT THE GAME")
        print(Fore.WHITE+"GAME OVER")
        print(Fore.BLUE+"YOUR SCORE: ",Fore.WHITE+str(score))
        sys.exit()
    if s!=0 and s!='b':
        # if move_type==1:
        #     man.set_detonation(man.activeBombs[0].get_detonation())
        b = man.Move(s,b,move_type)
        escaped = 1
        if flag == 1:
            for ele in Box[3]:
                if ele[0]==man.get_lefttop_x() and ele[1]==man.get_lefttop_y():
                    escaped = 0
                    break
        if escaped == 1:
            flag = 0
        if len(b)==2:
            b = b[0]             ##LENGTH OF TWO INDICATES BOMBERMAN COMMITED SUICIDE
            a.PrintBoard(b)
            max_lifes-=1
            Resetflag = 1
            CheckToEnd(max_lifes,enemies)
            if len(man.activeBombs)!=0:
                b = man.activeBombs[0].ClearGridOfPerson(b,0)
                if detonation == 3:
                    b = man.activeBombs[0].ClearGridAfterBlast(b,Box[3])
            temp = ResetGame(b,man)
            b = temp[0]
            man = temp[1]
            flag = 0
            Active = 0
            detonation = 0
        move_type = 0
    if Resetflag == 1:
        continue

    if s=='b':
        if len(man.activeBombs)==0:
            b = man.PlotBomb(b,1,3,2)
            man.set_detonation(2)
            move_type = 1
            Active = 1
            detonation = 0
    ##ENDINPUTPART

    ##ENEMYPART
    if time.time()>=NextInput:
        NextInput = time.time()+1
        Timer = Timer-1
        Synchronous=1
        Resetflag = 0
        for i in a.enemies:
            Resetflag = 0
            temp = i.RandomMove(b)
            b = i.Move(temp[0],b,temp[1])
            if temp[1] == 3:                                    ##THE ENEMY KILLED BOMBERMAN
                a.PrintBoard(b)
                max_lifes-=1
                Resetflag = 1
                if max_lifes == -1:
                    print(Fore.WHITE+"GAME OVER")
                    print(Fore.BLUE+"YOUR SCORE: ",Fore.WHITE+str(score))
                    sys.exit()
                if len(man.activeBombs)!=0:
                    b = man.activeBombs[0].ClearGridOfPerson(b,0)
                    if detonation == 3:
                        b = man.activeBombs[0].ClearGridAfterBlast(b,Box[3])
                temp = ResetGame(b,man)
                b = temp[0]
                man = temp[1]
                flag = 0
                Active = 0
                move_type = 0
                detonation = 0
                break
        if Resetflag == 1:
            continue
    ##ENEMYPARTENDS

    signal.alarm(0)
    os.system('clear')

##GAMEOWER
if Timer == -1:
    print(Fore.WHITE+"GAME OVER")
    print(Fore.BLUE+"YOUR SCORE: ",Fore.WHITE+str(score))
##ENDGAME

##ENDCODE
