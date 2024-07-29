import random
from edo_map import EdoMap

class TownMap(EdoMap):
    def __init__(self, width=160, height=40, load_filename=None):
        if load_filename:
            self.load_state(load_filename)
        else:
            self.town_name = self.random_town_name()
            self.buildings = []
            super().__init__(width, height)

    def random_town_name(self):
        town_names = ["Tokyo", "Kyoto", "Osaka", "Hiroshima", "Nara", "Nagoya", "Kobe", "Fukuoka", "Sapporo", "Sendai"]
        return random.choice(town_names)

    def tatami_size(self, num_tatami):
        if num_tatami < 6:
            raise ValueError("A room must have at least 6 tatami mats")
        tatami_length = 6
        tatami_width = 3
        total_area = num_tatami * tatami_length * tatami_width

        possible_sizes = []
        for width in range(tatami_width, 21, tatami_width):
            length = total_area // width
            if length >= 10 and length <= 20:
                possible_sizes.append((length, width))

        if not possible_sizes:
            raise ValueError("No valid room size could be determined")

        return random.choice(possible_sizes)

    def generate_map(self):
        self.place_buildings()
        self.place_streets()
        self.place_player()

    def place_buildings(self):
        num_buildings = random.randint(10, 20)
        for _ in range(num_buildings):
            shape = random.choice(['square', 'rectangle'])
            if shape == 'square':
                size = random.randint(1, 2)  # Square side length in spaces (each space is 3 feet)
                building_width = building_height = size * 3 + 2  # Add walls
            elif shape == 'rectangle':
                width = random.randint(1, 3)  # Width in spaces
                height = random.randint(1, 3)  # Height in spaces
                building_width = width * 3 + 2  # Add walls
                building_height = height * 3 + 2  # Add walls

            max_x = self.width - building_width - 3  # Ensure at least 2 spaces from the right edge
            max_y = self.height - building_height - 3  # Ensure at least 2 spaces from the bottom edge
            if max_x <= 2 or max_y <= 2:  # Ensure at least 2 spaces from the left and top edges
                continue
            x, y = None, None
            while True:
                x = random.randint(2, max_x)
                y = random.randint(2, max_y)
                if self.is_space_available(x, y, building_width, building_height):
                    break
            self.add_building(x, y, building_width, building_height)

    def is_space_available(self, x, y, width, height):
        for i in range(y - 2, y + height + 2):
            for j in range(x - 2, x + width + 2):
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.map[i][j] != ' ':
                        return False
        return True

    def add_building(self, x, y, width, height):
        door_side = random.choice(['top', 'bottom', 'left', 'right'])
        if door_side in ['top', 'bottom']:
            door_position = random.randint(x + 1, x + width - 2)
        else:
            door_position = random.randint(y + 1, y + height - 2)

        for i in range(y, y + height):
            for j in range(x, x + width):
                if i == y or i == y + height - 1 or j == x or j == x + width - 1:
                    if door_side == 'top' and i == y and j == door_position:
                        self.map[i][j] = '+'
                    elif door_side == 'bottom' and i == y + height - 1 and j == door_position:
                        self.map[i][j] = '+'
                    elif door_side == 'left' and j == x and i == door_position:
                        self.map[i][j] = '+'
                    elif door_side == 'right' and j == x + width - 1 and i == door_position:
                        self.map[i][j] = '+'
                    else:
                        self.map[i][j] = '#'
                else:
                    self.map[i][j] = ' '

    def place_streets(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == ' ' and (self.is_near_building(x, y)):
                    self.map[y][x] = '.'

    def is_near_building(self, x, y):
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                    if self.map[y + dy][x + dx] == '#':
                        return True
        return False

    def place_player(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.map[y][x] == ' ':
                self.map[y][x] = '@'
                self.player_x = x
                self.player_y = y
                break

    def save_state(self):
        filename = f"{self.town_name.replace(' ', '_')}.txt"
        with open(filename, "w") as file:
            for row in self.map:
                file.write("".join(row) + "\n")
            file.write(f"Town name: {self.town_name}\n")
            file.write(f"Player position: ({self.player_x}, {self.player_y})\n")

    def load_state(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            self.map = [list(line.rstrip()) for line in lines[:-2]]
            self.town_name = lines[-2].split(": ")[1].strip()
            player_position = lines[-1].split(": ")[1].strip()
            self.player_x, self.player_y = map(int, player_position.strip("()").split(", "))
            self.height = len(self.map)
            self.width = len(self.map[0]) if self.height > 0 else 0
            print(f"Loaded map with dimensions: {self.width}x{self.height}")
            print(f"Town name: {self.town_name}")
            print(f"Player position: ({self.player_x}, {self.player_y})")

    def micro_map(self, stdscr):
        screen_height, screen_width = stdscr.getmaxyx()
        scale_x = max(1, self.width // screen_width)
        scale_y = max(1, self.height // screen_height)

        for y in range(0, self.height, scale_y):
            for x in range(0, self.width, scale_x):
                micro_y = y // scale_y
                micro_x = x // scale_x
                if 0 <= micro_y < screen_height and 0 <= micro_x < screen_width:
                    try:
                        if self.map[y][x] == '#':
                            stdscr.addch(micro_y, micro_x, 'B')
                        elif self.map[y][x] == '@':
                            stdscr.addch(micro_y, micro_x, '@')
                        else:
                            stdscr.addch(micro_y, micro_x, ' ')
                    except curses.error:
                        pass  # Ignore drawing errors
