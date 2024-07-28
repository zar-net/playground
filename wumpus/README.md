# Hunt the Wumpus

Hunt the Wumpus is a text-based adventure game implemented using Python and ncurses. The player must navigate through a series of caves to find and shoot the Wumpus, avoiding pits and collecting gold along the way. I originally created this version as a foundation for a ROGUE-like game I want to build out and this was a model for a line of sight algorithm using  Bresenham’s line algorithm and ray casting

![wumpus_screen](https://github.com/user-attachments/assets/38b32cdc-447b-45c6-bee3-ef3347a2ccc9)

## Features

- **Randomly Generated Map**: The game generates a random map with caves, tunnels, walls, pits, and gold.
- **Player and Wumpus Movement**: The player can move around the map, and the Wumpus moves randomly with a chance to chase the player.
- **Arrow Shooting**: The player can shoot arrows to try to kill the Wumpus. The arrows travel in a straight line and stop at walls.
- **Visibility**: The player can see 5 spaces in all directions, but visibility is blocked by walls.
- **Map Revelation**: The map is revealed as the player moves, and revealed areas stay visible.

## Dependencies

- Python 3
- ncurses library

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/hunt-the-wumpus.git
    cd hunt-the-wumpus
    ```

2. **Ensure ncurses is installed**:
    ```sh
    sudo apt-get install libncurses5-dev libncursesw5-dev
    ```

## Running the Game

To run the game, execute the following command:
```sh
python game.py
```

### Controls

- **Arrow Keys**: Move the player.
- **W**: Shoot an arrow upwards.
- **S**: Shoot an arrow downwards.
- **A**: Shoot an arrow to the left.
- **D**: Shoot an arrow to the right.
- **Q**: Quit the game.

## File Structure

game.py: Contains the main game logic and the Game class.
player.py: Contains the Player class and player-specific logic.
wumpus.py: Contains the Wumpus class and Wumpus-specific logic.

## Gameplay

**Objective:** The goal is to find and shoot the Wumpus while avoiding pits and collecting gold.

**Movement:** Use the arrow keys to move around the map. The map is revealed as you move.

**Shooting Arrows:** Use the W, S, A, and D keys to shoot arrows in the respective directions. You have a limited number of arrows.

**Winning:** You win the game if you successfully shoot the Wumpus.

**Losing:** The game ends if you fall into a pit or are caught by the Wumpus.

