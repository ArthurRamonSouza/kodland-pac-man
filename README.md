# **Pac-Man Game**

A simple copy of the classic Pac-Man game made in Python using Pygame library.


## Main File

The menu is in the **main** file and have the code to make the initial menu of the game.

This menu have three option: **Start the Game**, **Show Instructions** and **Quit**.
Pressing the given key, you can navigate through the menu.

This file handles the Pygame loop.


## Pac-Man File

Contains the game logic and the initialization of the level, the player and the ghosts.
The responsibility for checking collisions, possible player positions, drawing elements on the screen and killing or being killed by the ghosts are here in this file.


## Ghost Class

Separated from pacman file to modularize code.
Contains the ghosts code to make them move through the level and be drawn in the screen.

## Borders File

Is just a big matrix that represents the initial state of the game level, where each number corresponds to a specific type of terrain, object, or border.
