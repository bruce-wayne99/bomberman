# PROJECT FILE

- Bomberman game
  - Played in a grid containing enemies which can be killed using bombs
  - Enemies are able to kill the bomberman when they meet the Bomberman
  - They are 3 levels implemented
  - Each level contains 3 lifes
  - After each level we get an extra life
  - Each level has a time limit of 200 seconds
  - 20 points for brick and 100 points for destroying enemy
  - Each level should be finished within the time given
  - You can be killed by an enemy whenever he approaches You
  - The bomb explodes in 3 frames (3 seconds here)

##Prerequisites
- python3 or ipython3
- colorama : pip install colorama
- getch : pip install getch
- os
- sys
- signal
- time
- random

##RULES
- 'a' for moving bomberman to left
- 'd' for moving bomberman to right
- 's' for moving bomberman down
- 'w' for moving bomberman up
- 'b' for plotting a bomb at the present position
##USAGE
 - In the bomberman directory run the game.py file
 - USAGE : "ipython3 game.py" (or) "python3 game.py"

##Implementation
 - 7 classes have been implemented for the game
 - enemy , bomberman inherit person class
 - board inherit walls,bricks classes
 - all the files are linked together in the game.py file

##BONUS IMPLEMENTATION
  - Implemented different colors for the enemies,board,bomberman,explosion,bomb
  - Implemented upto 3 levels of play
  - Implemented the counter for the bomb
