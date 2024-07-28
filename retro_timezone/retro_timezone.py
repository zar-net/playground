import curses
from datetime import datetime
import pytz
import argparse

def get_time_in_timezone(timezone):
    """
    Returns the current date, time, and timezone abbreviation for the given timezone.
    If the timezone abbreviation is 3 characters, adds an extra space for alignment.
    """
    tz = pytz.timezone(timezone)
    time_in_tz = datetime.now(tz)
    date_str = time_in_tz.strftime('%Y-%m-%d')
    time_str = time_in_tz.strftime('%H:%M:%S')
    tz_name = time_in_tz.tzname()
    if len(tz_name) == 3:
        tz_name += ' '
    return date_str, time_str, tz_name

def center_text(text, width):
    """
    Centers the given text within the given width.
    Adds spaces on both sides if the text is shorter than the width.
    Ensures that the text is properly centered and the borders are consistent.
    """
    if len(text) >= width:
        return text
    total_spaces = width - len(text)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    return ' ' * left_spaces + text + ' ' * right_spaces

def main(stdscr, color_pair, specified_width):
    """
    Main function to display the time zone information using ncurses.
    Initializes colors, sets up the layout, and updates the display in a loop.
    """
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(1000)

    # Initialize color pairs
    curses.start_color()
    if color_pair == 1:
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Amber
    elif color_pair == 2:
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green

    # Define time zones to display
    timezones = [
        ('UK', 'Europe/London'),
        ('Italy', 'Europe/Rome'),
        ('Toronto', 'America/Toronto'),
        ('New York', 'America/New_York'),
        ('Tokyo', 'Asia/Tokyo'),
        ('Sydney', 'Australia/Sydney'),
        # Add more timezones as needed
    ]

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        actual_screen_width = width - 4  # Calculate actual screen width

        # Set box dimensions based on the actual screen width
        max_columns = 3 if specified_width == 80 else 4  # Number of boxes per row
        box_width = (actual_screen_width - (max_columns - 1) - 2) // max_columns  # Fixed width for each box with one space between boxes and boundary
        box_height = 6  # Fixed height for each box

        # Draw borders
        stdscr.border(0)

        # Title
        title = "Retro Time Zone Display"
        stdscr.addstr(0, (width // 2) - (len(title) // 2), title, curses.A_BOLD | curses.color_pair(1))

        row = 0
        col = 0
        for name, tz in timezones:
            if (row + 1) * (box_height + 2) > height - 2:  # Adjust row height to include boundary
                break

            date_str, time_str, tz_name = get_time_in_timezone(tz)
            start_y = row * (box_height + 2) + 2  # Start position with 2 spaces top margin and 1 space boundary
            start_x = col * (box_width + 2) + 2   # Start position with 2 spaces left margin and 1 space boundary
            stdscr.addstr(start_y, start_x, "+" + "-" * box_width + "+", curses.color_pair(1))
            stdscr.addstr(start_y + 1, start_x, f"|{center_text(name, box_width)}|", curses.color_pair(1))
            stdscr.addstr(start_y + 2, start_x, f"|{center_text(tz_name, box_width)}|", curses.color_pair(1))
            stdscr.addstr(start_y + 3, start_x, f"|{center_text(date_str, box_width)}|", curses.color_pair(1))
            stdscr.addstr(start_y + 4, start_x, f"|{center_text(time_str, box_width)}|", curses.A_BOLD | curses.color_pair(1))
            stdscr.addstr(start_y + 5, start_x, "+" + "-" * box_width + "+", curses.color_pair(1))

            col += 1
            if col >= max_columns:
                col = 0
                row += 1

        # Footer
        footer = "Press 'q' to quit"
        stdscr.addstr(height - 1, (width // 2) - (len(footer) // 2), footer, curses.A_BOLD | curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Retro Time Zone Display')
    parser.add_argument('--color', choices=['amber', 'green'], default='amber', help='Set the display color (amber or green)')
    parser.add_argument('--width', type=int, choices=[80, 120], default=80, help='Set the display width (80 or 120 columns)')
    args = parser.parse_args()

    color_pair = 1 if args.color == 'amber' else 2
    specified_width = args.width

    # Run the ncurses application
    curses.wrapper(main, color_pair, specified_width)

