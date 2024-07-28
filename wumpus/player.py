import curses

class Player:
    def __init__(self, start_pos):
        self.position = start_pos
        self.arrows = 2

    def move(self, direction, game):
        new_pos = self.position[:]
        if direction == 'UP' and self.position[1] > 0:
            new_pos[1] -= 1
        elif direction == 'DOWN' and self.position[1] < len(game.map) - 1:
            new_pos[1] += 1
        elif direction == 'LEFT' and self.position[0] > 0:
            new_pos[0] -= 1
        elif direction == 'RIGHT' and self.position[0] < len(game.map[0]) - 1:
            new_pos[0] += 1
        if game.map[new_pos[1]][new_pos[0]] == '.':
            self.position = new_pos
            game.reveal_map(self.position[0], self.position[1])
            game.draw_map()

    def shoot_arrow(self, direction, game):
        if self.arrows > 0:
            arrow_pos = self.position[:]
            arrow_char = '|' if direction in ['UP', 'DOWN'] else '-'
            original_char = game.map[arrow_pos[1]][arrow_pos[0]]
            while True:
                game.stdscr.addch(arrow_pos[1], arrow_pos[0], original_char, curses.color_pair(5))
                game.stdscr.refresh()

                if direction == 'UP' and arrow_pos[1] > 0:
                    arrow_pos[1] -= 1
                elif direction == 'DOWN' and arrow_pos[1] < len(game.map) - 1:
                    arrow_pos[1] += 1
                elif direction == 'LEFT' and arrow_pos[0] > 0:
                    arrow_pos[0] -= 1
                elif direction == 'RIGHT' and arrow_pos[0] < len(game.map[0]) - 1:
                    arrow_pos[0] += 1
                else:
                    break

                if game.map[arrow_pos[1]][arrow_pos[0]] == '#':
                    break  # Arrow hits a wall

                if arrow_pos in game.wumpus.positions:
                    game.win = True
                    game.game_over = True
                    break

                # Draw arrow and refresh screen to show movement
                original_char = game.map[arrow_pos[1]][arrow_pos[0]]
                game.stdscr.addch(arrow_pos[1], arrow_pos[0], arrow_char, curses.color_pair(3))
                game.stdscr.refresh()
                curses.napms(50)  # Pause for a short period to show arrow movement

            self.arrows -= 1
            game.draw_map()  # Redraw map to remove the arrow after shooting
