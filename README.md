# Python Type Typing Ninja !
#### Video Demo : 
#### Description:
In Python Type Typing Ninja, Daimyo Python sent his Ninjas and Samurai to raid your home for your food ! In this class 
conflict, you'll have to defeat the noble's baddies to keep your precious sunflower oil and french mustard. To knock'em 
out, you'll have to type their python type before they reach the noble's side (Far right, obviously)
I'm using zlib toi compress images, pygames, random ton span enemies at random and at ramdom locations. I worked alone
and used a sprite set under CC0 licence, organized in sprite sheet pour ennemies' animations.

## Goals
* Learn Pygame
* develop some function du split sprite-sheets
* Try some basic animation
* Learn ho to manipulate text in pygame
* Learn how to interact with the screen by mouse AND keyboard

## Constrains
* No other external library than Pygame
* No other external files that requirements and README.md
* In less than 3 days
## Credits:
* Library [pygame](https://www.pygame.org)
* Enemies' sprites: Ninja Adventure Asset Pack [Pixel-boy](https://pixel-boy.itch.io/) (CC0)

### More infos
The code is organized in 5 classes and 3 functions
#### Classes:
**Player()** representing the player, to manage the score and later the name, and maybe playable character if I want add 
some dodging mechanics on top of the typing

**Enemy()** representing the enemy. It contains all the position info, animation, spritesheet extracting, word to type, HP
and a method to draw himself on the screen. Enemies are instanciated by spawner() function in the game loop into a list.

**Button()** contain the image and logic of a button. It can draw himself on the screen too calling the draw method.
al callback function is pased as a string and eval is used to execute the code.

**Title()** and **Intro()** are here to write the title and intro text when initialized and called.
#### Functions:
**switch_game_status(status)** change the current state of the game. "START" for the gameplay loop, "GAMEOVER" for the 
Game-over screen and "MENU" for the main menu

**spawner(entities)** generate enemies un the list passed in first argument at predefined intervals and scale the
difficulty(speed) of the enemies based on the player score.

**enemy_garbage_collector(enemies)** scan all the entities in the list passed as first argument, if they are at 0 HP, 
they are .pop()'ed and player score incremented by 1. 

### TODO
* Find optimisations
* Balance difficulty
* Difficulty selection
* Find a way to generate background music without external files
* Background for the menus and gameplay screens
* Bonuses
* Playable characters
* Dodging mechanics
* Refine enemy's text display

