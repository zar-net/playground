import random
import curses

class Wumpus:
    def __init__(self, positions):
        self.positions = positions
        self.chase = False
        self.chase_count = 0

    def move(self, player_pos, game_map):
        for i in range(len(self.positions)):
            if self.chase:
                self.chase_count += 1
                if self.chase_count > 3:
                    self.chase = False
                    self.chase_count = 0

            if self.chase:
                self.move_towards_player(i, player_pos, game_map)
            else:
                if random.random() < 0.8:
                    self.move_random(i, game_map)
                else:
                    self.chase = True

    def move_random(self, i, game_map):
        directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        direction = random.choice(directions)
        self.move_entity(self.positions[i], direction, game_map)

    def move_towards_player(self, i, player_pos, game_map):
        if self.positions[i][0] < player_pos[0]:
            self.move_entity(self.positions[i], 'RIGHT', game_map)
        elif self.positions[i][0] > player_pos[0]:
            self.move_entity(self.positions[i], 'LEFT', game_map)
        elif self.positions[i][1] < player_pos[1]:
            self.move_entity(self.positions[i], 'DOWN', game_map)
        elif self.positions[i][1] > player_pos[1]:
            self.move_entity(self.positions[i], 'UP', game_map)

    def move_entity(self, pos, direction, game_map):
        new_pos = pos[:]
        if direction == 'UP' and pos[1] > 0:
            new_pos[1] -= 1
        elif direction == 'DOWN' and pos[1] < len(game_map) - 1:
            new_pos[1] += 1
        elif direction == 'LEFT' and pos[0] > 0:
            new_pos[0] -= 1
        elif direction == 'RIGHT' and pos[0] < len(game_map[0]) - 1:
            new_pos[0] += 1
        if game_map[new_pos[1]][new_pos[0]] == '.':
            pos[0], pos[1] = new_pos
