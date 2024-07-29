import curses
import argparse
from town_map import TownMap

def main(stdscr, load_filename=None):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(100)  # Refresh every 100 ms

    town = TownMap(load_filename=load_filename) if load_filename else TownMap()

    offset_x = 0
    offset_y = 0
    show_micro_map = False

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if show_micro_map:
            town.micro_map(stdscr)
        else:
            town.draw(stdscr, offset_x, offset_y)
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
        elif not show_micro_map:
            if key == curses.KEY_UP:
                offset_y = max(0, offset_y - 1)
            elif key == curses.KEY_DOWN:
                offset_y = min(town.height - height, offset_y + 1)
            elif key == curses.KEY_LEFT:
                offset_x = max(0, offset_x - 1)
            elif key == curses.KEY_RIGHT:
                offset_x = min(town.width - width, offset_x + 1)

        stdscr.refresh()

    town.save_state()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Edo Town Map")
    parser.add_argument("-L", "--load", type=str, help="Load a saved map from a file")
    args = parser.parse_args()

    curses.wrapper(main, load_filename=args.load)
