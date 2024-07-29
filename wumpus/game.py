import curses
import random
from player import Player
from wumpus import Wumpus

# Game constants
MAP_WIDTH = 80
MAP_HEIGHT = 20
PIT_COUNT = 2
GOLD_COUNT = 1
MIN_CAVE_COUNT = 10
MAX_CAVE_COUNT = 20
VISIBILITY_RANGE = 5

class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.map = [[' ' for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        self.revealed_map = [[' ' for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        self.caves = []
        self.tunnels = []
        self.player = None
        self.wumpus = None
        self.pit_pos = []
        self.gold_pos = []
        self.game_over = False
        self.win = False
        self.init_game()

    def init_game(self):
        self.stdscr.scrollok(False)  # Turn off scrolling
        max_y, max_x = self.stdscr.getmaxyx()
        if max_y < MAP_HEIGHT or max_x < MAP_WIDTH:
            raise ValueError("Terminal size is too small for the map dimensions.")
        
        # Initialize color pairs
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)    # Wumpus
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)  # Pit
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Player
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK) # Gold
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Empty space
        curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Wall

        # Create caves and tunnels
        self.create_caves_and_tunnels()

        # Initialize player, wumpus, pit, and gold positions
        self.player = Player(random.choice(self.caves))
        self.wumpus = Wumpus(self.random_positions(1))
        self.pit_pos = self.random_positions(PIT_COUNT)
        self.gold_pos = self.random_positions(GOLD_COUNT)

        # Reveal initial player position
        self.reveal_map(self.player.position[0], self.player.position[1])

    def create_caves_and_tunnels(self):
        # Randomly determine the number of caves
        cave_count = random.randint(MIN_CAVE_COUNT, MAX_CAVE_COUNT)

        # Create caves
        for _ in range(cave_count):
            x = random.randint(1, MAP_WIDTH - 2)
            y = random.randint(1, MAP_HEIGHT - 2)
            self.caves.append([x, y])
            self.map[y][x] = '.'

        # Create tunnels between caves
        for cave in self.caves:
            target_cave = random.choice(self.caves)
            while target_cave == cave:
                target_cave = random.choice(self.caves)
            self.tunnels.append((cave, target_cave))
            self.create_tunnel(cave, target_cave)

        # Add walls around caves and tunnels
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                if self.map[y][x] == '.':
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            ny, nx = y + dy, x + dx
                            if 0 <= ny < MAP_HEIGHT and 0 <= nx < MAP_WIDTH and self.map[ny][nx] == ' ':
                                self.map[ny][nx] = '#'

    def create_tunnel(self, cave1, cave2):
        # Create a tunnel between two caves
        x1, y1 = cave1
        x2, y2 = cave2
        while x1 != x2 or y1 != y2:
            if x1 < x2:
                x1 += 1
            elif x1 > x2:
                x1 -= 1
            elif y1 < y2:
                y1 += 1
            elif y1 > y2:
                y1 -= 1
            self.map[y1][x1] = '.'

    def random_positions(self, count):
        # Generate random positions for game elements
        positions = []
        while len(positions) < count:
            pos = random.choice(self.caves)
            if pos not in positions and pos != self.player.position:
                positions.append(pos)
        return positions

    def draw_map(self):
        # Clear the screen
        self.stdscr.clear()

        # Draw the revealed map with colors
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                if [x, y] == self.player.position:
                    
                    self.stdscr.attron(curses.color_pair(3))
                    self.stdscr.addch(y, x, '@')
                    self.stdscr.attroff(curses.color_pair(3))
                    
                elif self.revealed_map[y][x] != ' ':
                    if [x, y] in self.wumpus.positions:
                        self.stdscr.attron(curses.color_pair(1))
                        self.stdscr.addch(y, x, 'W')
                        self.stdscr.attroff(curses.color_pair(1))                        
                    elif [x, y] in self.pit_pos:
                        self.stdscr.attron(curses.color_pair(2))
                        self.stdscr.addch(y, x, 'P')
                        self.stdscr.attroff(curses.color_pair(2))                        
                    elif [x, y] in self.gold_pos:
                        self.stdscr.attron(curses.color_pair(4))
                        self.stdscr.addch(y, x, 'G')
                        self.stdscr.attroff(curses.color_pair(4))                        
                    elif self.map[y][x] == '.':
                        self.stdscr.attron(curses.color_pair(5))
                        self.stdscr.addch(y, x, '.')
                        self.stdscr.attroff(curses.color_pair(5))   
                    elif self.map[y][x] == '#':
                        self.stdscr.attron(curses.color_pair(6))
                        self.stdscr.addch(y, x, '#')
                        self.stdscr.attroff(curses.color_pair(6)) 

        # Display the number of arrows left
        self.stdscr.addstr(0, 0, f'Arrows: {self.player.arrows}', curses.color_pair(3))
        self.stdscr.refresh()

    def reveal_map(self, px, py):
        # Reveal the map around the player's position
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
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

    def check_positions(self):
        # Check for game-over conditions
        if self.player.position in self.wumpus.positions:
            self.game_over = True
        elif self.player.position in self.pit_pos:
            self.game_over = True
        elif self.player.position in self.gold_pos:
            self.win = True
            self.game_over = True

    def game_loop(self):
        # Main game loop
        while not self.game_over:
            self.draw_map()
            key = self.stdscr.getch()
            if key == curses.KEY_UP:
                self.player.move('UP', self)
            elif key == curses.KEY_DOWN:
                self.player.move('DOWN', self)
            elif key == curses.KEY_LEFT:
                self.player.move('LEFT', self)
            elif key == curses.KEY_RIGHT:
                self.player.move('RIGHT', self)
            elif key in [ord('w'), ord('W')]:
                self.player.shoot_arrow('UP', self)
            elif key in [ord('s'), ord('S')]:
                self.player.shoot_arrow('DOWN', self)
            elif key in [ord('a'), ord('A')]:
                self.player.shoot_arrow('LEFT', self)
            elif key in [ord('d'), ord('D')]:
                self.player.shoot_arrow('RIGHT', self)
            elif key in [ord('q'), ord('Q')]:
                self.game_over = True
            self.wumpus.move(self.player.position, self.map)
            self.check_positions()

        self.draw_map()
        if self.win:
            self.stdscr.addstr(MAP_HEIGHT // 2, MAP_WIDTH // 2 - 4, "You Win!", curses.color_pair(3) | curses.A_BOLD)
        else:
            self.stdscr.addstr(MAP_HEIGHT // 2, MAP_WIDTH // 2 - 4, "Game Over!", curses.color_pair(3) | curses.A_BOLD)
        self.stdscr.refresh()
        self.stdscr.getch()

def main(stdscr):
    # Initialize curses and start the game
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    game = Game(stdscr)
    game.game_loop()

curses.wrapper(main)
