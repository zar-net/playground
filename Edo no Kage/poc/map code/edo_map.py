import curses

class EdoMap:
    def __init__(self, width=160, height=40):
        self.width = width
        self.height = height
        self.map = [[' ' for _ in range(width)] for _ in range(height)]
        self.generate_map()

    def generate_map(self):
        raise NotImplementedError("Subclasses should implement this method")

    def draw(self, stdscr, offset_x=0, offset_y=0):
        screen_height, screen_width = stdscr.getmaxyx()
        for y in range(screen_height):
            for x in range(screen_width):
                map_y = y + offset_y
                map_x = x + offset_x
                if 0 <= map_y < self.height and 0 <= map_x < self.width:
                    try:
                        stdscr.addch(y, x, self.map[map_y][map_x])
                    except curses.error:
                        pass  # Ignore drawing errors
