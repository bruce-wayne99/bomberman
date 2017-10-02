# BEGIN CODE

# PACKAGES
import os
import sys
import signal
import time
from colorama import Fore
from getch import getch
from random import random
# PACKAGES

# CLASSES
from board import Board
from bomb import Bomb
from person import Person
from bomberman import Bomberman
from enemy import Enemy


# USED FOR TAKING INPUTS
TIMEOUT = 1             # TIMEOUT indicates the speed of the enemy

''' interrupted is a function which is called if the input is not given
    within 1 second of time
'''


def interrupted(signum, frame):
    return 'interrupted'

# Indicates the implementation of the timeframe


signal.signal(signal.SIGALRM, interrupted)

''' input_char is the function used to take the input which returns the character
    that is entered otherwise returns a zero(null)
'''


def input_char():
    try:
        foo = getch()
        return foo
    except BaseException:
        return 0


# Globally used variable DECLARATIONS
Level = 1
max_lifes = 2
TotalScore = 0
max_enemies = 6
brickslimit = 40

# BEGIN GAME

while Level <= 3:

    # DECLARATIONS for each level

    a = Board(42, 84, brickslimit, 2, 4)
    b = a.CreateEmptyBoard()
    b = a.PopulateBoardWithWalls(b)
    b = a.PopulateBoardWithBricks(b)
    man = Bomberman(2, 4, 1)
    b = man.PopulateGridWithPerson(b)
    b = a.PopulateBoardWithEnemies(b, max_enemies)
    enemies = len(a.enemies)
    count = 0
    detonation = 0  # Used as a detonator for the bomb
    Active = 0      # Indicates whether the bomb is active or not
    move_type = 0   # Indicates the type of move
    score = 0       # Indicates the score of each level
    flag = 0
    Resetflag = 0   # Used to call ResetGame function
    NextInput = time.time() + 1
    ''' This is a flag used to allow Synchronous motion of the enemies and bomb
        detonation
    '''
    Synchronous = 0
    Timer = 200

    # ResetGame is used to reset the game whenever the bomberman dies
    def ResetGame(grid, man):
        man = Bomberman(2, 4, 1)
        grid = man.PopulateGridWithPerson(grid)
        return [grid, man]

    ''' This function is used to check if the lifes are over or all the
        enemies are dead
    '''
    def CheckToEnd(max_lifes, enemies):
        if max_lifes == -1:
            a.PrintBoard(b)
            print(Fore.WHITE + "GAME OVER")
            print(Fore.BLUE + "YOUR SCORE: ",
                  Fore.WHITE + str(TotalScore + score))
            sys.exit()
        if enemies == 0:
            return 1
        else:
            return 0

    while Timer >= 0:
        # LEVEL BEGINS

        # SETTING THE INPUT TIME LIMIT
        signal.alarm(TIMEOUT)

        ''' The above statement is used to set the Timer
        '''
        # PRINT_PART

        a.PrintBoard(b)
        print(Fore.RED + "LIFES AVAILABLE : ",
              Fore.WHITE + str(max_lifes),
              '\t',
              Fore.MAGENTA + "YOUR SCORE : ",
              Fore.WHITE + str(TotalScore + score),
              '\t',
              Fore.GREEN + "TIME : ",
              Fore.WHITE + str(Timer),
              '\t',
              Fore.CYAN + "LEVEL :",
              Fore.WHITE + str(Level))

        # END_PRINT_PART

        # BOMBPART

        if Active == -1:
            Active = 0
            detonation = 0
            b = man.activeBombs[0].ClearGridAfterBlast(b, Box[3])
            man.activeBombs = []
            if flag == 1:
                max_lifes -= 1
                CheckToEnd(max_lifes, enemies)
                man = Bomberman(2, 4, 1)
                b = man.PopulateGridWithPerson(b)
                move_type = 0
                flag = 0

        ''' If the active flag is set to -1 then it indicates the bomb has
            blasted and we need to clear the blast area
        '''
        if Synchronous == 1:
            Synchronous = 0
            NextInput = time.time() + 1
            if Active == 1:
                flag = 0
                detonation += 1
                Box = man.activeBombs[0].CheckIfTime(
                    b, detonation, enemies, 1, score)
                b = Box[0]
                score = Box[5]
                if len(Box[3]) == 0:
                    man.activeBombs[0].set_detonation(
                        man.activeBombs[0].get_detonation() - 1)
                    man.set_detonation(man.get_detonation() - 1)
                    if move_type != 1:
                        b = man.activeBombs[0].ClearGridOfPerson(b, 1)
                if len(Box[3]) != 0:
                    Active = -1
                    if Box[2] == 0:
                        flag = 1
                    for num in Box[4]:
                        a.RemoveEnemyFromList(num[0], num[1])
                        score += 100
                        enemies -= 1
            if CheckToEnd(max_lifes, enemies) == 1:
                break

        # INPUTPART
        Synchronous = 0
        Resetflag = 0
        s = input_char()
        if s == 'q':
            print(Fore.RED + "YOU QUIT THE GAME")
            print(Fore.WHITE + "GAME OVER")
            print(Fore.BLUE + "YOUR SCORE: ",
                  Fore.WHITE + str(TotalScore + score))
            sys.exit()
        if s != 0 and s != 'b':
            b = man.Move(s, b, move_type)
            escaped = 1
            if flag == 1:
                for ele in Box[3]:
                    if ele[0] == man.get_lefttop_x(
                    ) and ele[1] == man.get_lefttop_y():
                        escaped = 0
                        break
            if escaped == 1:  # If the bomberman escaped the blast
                flag = 0
            if len(b) == 2:
                b = b[0]
                a.PrintBoard(b)
                print(Fore.RED +
                      "LIFES AVAILABLE : ", Fore.WHITE +
                      str(max_lifes), '\t', Fore.MAGENTA +
                      "YOUR SCORE : ", Fore.WHITE +
                      str(TotalScore +
                          score), '\t', Fore.GREEN +
                      "TIME : ", Fore.WHITE +
                      str(Timer), '\t', Fore.CYAN +
                      "LEVEL :", Fore.WHITE +
                      str(Level))
                # LENGTH OF TWO INDICATES BOMBERMAN COMMITED SUICIDE
                max_lifes -= 1
                Resetflag = 1
                CheckToEnd(max_lifes, enemies)
                if len(man.activeBombs) != 0:
                    b = man.activeBombs[0].ClearGridOfPerson(b, 0)
                    if detonation == 3:
                        b = man.activeBombs[0].ClearGridAfterBlast(b, Box[3])
                temp = ResetGame(b, man)
                b = temp[0]
                man = temp[1]
                flag = 0
                Active = 0
                detonation = 0
            move_type = 0
        if Resetflag == 1:
            continue

        if s == 'b':
            if len(man.activeBombs) == 0:
                b = man.PlotBomb(b, 1, 3, 2)
                man.set_detonation(2)
                move_type = 1
                Active = 1
                detonation = 0

        # ENEMYPART

        ''' This is used to check whether 1 sec has elapsed to move the enemy
            again
        '''
        if time.time() >= NextInput:
            NextInput = time.time() + 1
            Timer = Timer - 1
            Synchronous = 1
            Resetflag = 0
            for i in a.enemies:
                Resetflag = 0
                temp = i.RandomMove(b)
                b = i.Move(temp[0], b, temp[1])
                if temp[1] == 3:
                    a.PrintBoard(b)
                    print(Fore.RED +
                          "LIFES AVAILABLE : ", Fore.WHITE +
                          str(max_lifes), '\t', Fore.MAGENTA +
                          "YOUR SCORE : ", Fore.WHITE +
                          str(TotalScore +
                              score), '\t', Fore.GREEN +
                          "TIME : ", Fore.WHITE +
                          str(Timer), '\t', Fore.CYAN +
                          "LEVEL :", Fore.WHITE +
                          str(Level))  # THE ENEMY KILLED BOMBERMAN
                    max_lifes -= 1
                    Resetflag = 1
                    if max_lifes == -1:
                        print(Fore.WHITE + "GAME OVER")
                        print(Fore.BLUE + "YOUR SCORE: ",
                              Fore.WHITE + str(TotalScore + score))
                        sys.exit()
                    if len(man.activeBombs) != 0:
                        b = man.activeBombs[0].ClearGridOfPerson(b, 0)
                        if detonation == 3:
                            b = man.activeBombs[0].ClearGridAfterBlast(
                                b, Box[3])
                    temp = ResetGame(b, man)
                    b = temp[0]
                    man = temp[1]
                    flag = 0
                    Active = 0
                    move_type = 0
                    detonation = 0
                    break
            if Resetflag == 1:
                continue

        signal.alarm(0)     # Disabling the alarm
        os.system('clear')  # Used to clear the shell screen
    TotalScore += score     # Adding the score to the total score
    Level += 1
    max_lifes += 1  # AFTER CROSSING EACH LEVEL WE GET AN EXTRA LIFE
    brickslimit += 10   # Increased the brickslimit after each level
    max_enemies += 3    # Increased the number of enemies after each level
    # LEVELCOMPLETED
    if Timer == -1:
        print(Fore.WHITE + "GAME OVER")
        print(Fore.BLUE + "YOUR SCORE: ", Fore.WHITE + str(TotalScore))
        sys.exit()

print(Fore.WHITE + "GAME OVER")
print(Fore.BLUE + "YOUR SCORE: ", Fore.WHITE + str(TotalScore))

# ENDGAME

# ENDCODE
