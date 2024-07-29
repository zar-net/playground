import curses

# Quotes from Sun Tzu
quotes = [
    "The supreme art of war is to subdue the enemy without fighting.",
    "All warfare is based on deception.",
    "In the midst of chaos, there is also opportunity.",
    "Appear weak when you are strong, and strong when you are weak."
]

def main(stdscr):
    # Clear screen
    stdscr.clear()
    
    # Start color in curses
    curses.start_color()
    
    # Define color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Display the quotes in different colors and styles
    colors = [1, 2, 3, 4, 5]
    bg_colors = [6, 7, 8, 9, 10]
    
    for i, quote in enumerate(quotes):
        # Set color and addstr
        stdscr.attron(curses.color_pair(colors[i % len(colors)]))
        stdscr.addstr(i * 2, 0, quote)
        stdscr.attroff(curses.color_pair(colors[i % len(colors)]))

        # Set background color and addstr
        stdscr.attron(curses.color_pair(bg_colors[i % len(bg_colors)]))
        stdscr.addstr(i * 2 + 1, 0, quote)
        stdscr.attroff(curses.color_pair(bg_colors[i % len(bg_colors)]))

    # Display a quote in bold
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(len(quotes) * 2, 0, "Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win.")
    stdscr.attroff(curses.A_BOLD)

    # Refresh to show changes
    stdscr.refresh()

    # Wait for user input
    stdscr.getch()

# Start the curses application
curses.wrapper(main)
