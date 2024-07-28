## Line of Sight Algorithm

The game uses a **Ray Casting** algorithm to determine the player's visibility within the map. This algorithm ensures that the player can only see areas within a certain range, and visibility is blocked by walls.

### How the Ray Casting Algorithm Works

1. **Visibility Range**: The player has a visibility range of 5 tiles in all directions (up, down, left, right, and diagonals).

2. **Ray Casting**: For each direction from the player’s position, the algorithm casts a "ray" outward tile by tile.

3. **Boundary Check**: As the ray extends, it checks whether the current tile is within the map boundaries to avoid out-of-bounds errors.

4. **Wall Blocking**: If the ray encounters a wall (`#`), it stops. This ensures that areas beyond the wall remain unrevealed.

5. **Revealing Tiles**: All tiles within the visibility range and not blocked by walls are marked as revealed on the map.

### Ray Casting Algorithm Implementation

The Ray Casting algorithm is implemented in the `reveal_map` method of the `Game` class:

```python
def reveal_map(self, px, py):
    # Define the eight primary directions for ray casting
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]
    # For each direction, cast a ray
    for dx, dy in directions:
        x, y = px, py
        for _ in range(VISIBILITY_RANGE):
            x += dx
            y += dy
            if 0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT:
                self.revealed_map[y][x] = self.map[y][x]
                if self.map[y][x] == '#':
                    break
            else:
                break
```

### Example
Imagine the player (@) is at position (10, 10) on a 20x20 map, with a wall blocking part of the view:

```
Before Moving:
####################
#..................#
#..#####...........#
#..#...#...........#
#..#.@.#...........#
#..#####...........#
#..................#
#..................#
####################

After Moving:
####################
#..................#
#..#####...........#
#..#...#...........#
#..#...#...........#
#..#####...........#
#..................#
#..................#
####################
```

In this example, the wall at position (4, 2) blocks the player's view beyond it. The algorithm stops revealing tiles further in that direction, ensuring that the player cannot see past walls.

## Benefits of the Line of Sight Algorithm

**Realistic Visibility:** The algorithm simulates realistic visibility, enhancing the gameplay experience.

**Performance:** The ray casting approach is computationally efficient, allowing the game to run smoothly even with frequent player movements.

**Strategy:** Players must strategically navigate around walls to reveal new areas, adding a layer of depth to the game.
