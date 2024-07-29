import curses
import argparse
from town_map import TownMap

def get_door_direction(stdscr):
    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP:
            return (0, -1)
        elif key == curses.KEY_DOWN:
            return (0, 1)
        elif key == curses.KEY_LEFT:
            return (-1, 0)
        elif key == curses.KEY_RIGHT:
            return (1, 0)

def main(stdscr, load_filename=None):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(100)  # Refresh every 100 ms

    town = TownMap(load_filename=load_filename) if load_filename else TownMap()

    offset_x = 0
    offset_y = 0
    show_micro_map = False
    town.original_char = ' '

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if show_micro_map:
            town.micro_map(stdscr)
        else:
            town.draw(stdscr, offset_x, offset_y)
            building_name = town.in_building()
            if building_name:
                stdscr.addstr(0, 0, f"Town: {town.town_name} -- Building: {building_name}")
            else:
                stdscr.addstr(0, 0, f"Town: {town.town_name}")

        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key == ord('M'):
            show_micro_map = not show_micro_map
        elif key == 27:  # ESC key
            show_micro_map = False
        elif key == ord('R'):
            stdscr.clear()  # Clear the screen to refresh
        elif key == ord('o'):  # Open door
            direction = get_door_direction(stdscr)
            town.open_door(direction)
        elif key == ord('c'):  # Close door
            direction = get_door_direction(stdscr)
            town.close_door(direction)
        elif not show_micro_map:
            if key == curses.KEY_UP:
                town.move_player(0, -1)
            elif key == curses.KEY_DOWN:
                town.move_player(0, 1)
            elif key == curses.KEY_LEFT:
                town.move_player(-1, 0)
            elif key == curses.KEY_RIGHT:
                town.move_player(1, 0)

            # Update offset for scrolling
            if town.player_x < offset_x + 2:
                offset_x = max(0, town.player_x - 2)
            elif town.player_x > offset_x + width - 3:
                offset_x = min(town.width - width, town.player_x - width + 3)
            if town.player_y < offset_y + 2:
                offset_y = max(0, town.player_y - 2)
            elif town.player_y > offset_y + height - 3:
                offset_y = min(town.height - height, town.player_y - height + 3)

        stdscr.refresh()

    town.save_state()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Edo Town Map")
    parser.add_argument("-L", "--load", type=str, help="Load a saved map from a file")
    args = parser.parse_args()

    curses.wrapper(main, load_filename=args.load)
