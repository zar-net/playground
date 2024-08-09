import curses

# Sample data for demonstration
items = [
    {"col1": "Item 1", "col2": "Data 1", "col3": "Info 1", "col4": "Detail 1"},
    {"col1": "Item 2", "col2": "Data 2", "col3": "Info 2", "col4": "Detail 2"},
    {"col1": "Item 3", "col2": "Data 3", "col3": "Info 3", "col4": "Detail 3"},
    {"col1": "Item 4", "col2": "Data 4", "col3": "Info 4", "col4": "Detail 4"},
]

def draw_prompt(stdscr, prompt_text, key=None):
    h, w = stdscr.getmaxyx()
    if h > 1 and w > 10:  # Ensure there is enough space to draw the prompt
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(h-1, 0, " " * (w - 1))  # Clear the prompt area
        if key and 32 <= key <= 126:  # Only display printable characters
            stdscr.addstr(h-1, 2, f"[{prompt_text}{chr(key)}]".ljust(w - 4))
        else:
            stdscr.addstr(h-1, 2, f"[{prompt_text}>]".ljust(w - 4))
        stdscr.attroff(curses.color_pair(3))
        stdscr.refresh()

def main_menu(stdscr):
    curses.curs_set(0)  # Hide the cursor
    curses.start_color()  # Enable color
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)

    selected_row_idx = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        if h < 10 or w < 40:
            stdscr.addstr(0, 0, "Window size is too small")
            stdscr.refresh()
            continue

        # Draw single-line border around the screen
        stdscr.border()

        # Display the menu title
        title = "Demo Curses UI - Main Menu"
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(1, w//2 - len(title)//2, title)
        stdscr.attroff(curses.color_pair(1))

        # Display the list of items
        for idx, item in enumerate(items):
            x = 3
            y = idx + 3
            if idx == selected_row_idx:
                stdscr.attron(curses.color_pair(2))
            stdscr.addstr(y, x, f"{item['col1']:<10}{item['col2']:<10}{item['col3']:<10}{item['col4']:<10}")
            if idx == selected_row_idx:
                stdscr.attroff(curses.color_pair(2))

        draw_prompt(stdscr, " ")

        # Wait for user input
        key = stdscr.getch()
        draw_prompt(stdscr, ">", key)

        if key == curses.KEY_UP and selected_row_idx > 0:
            selected_row_idx -= 1
        elif key == curses.KEY_DOWN and selected_row_idx < len(items) - 1:
            selected_row_idx += 1
        elif key == ord('i'):  # Interact with the item
            curses.napms(500)
            edit_screen(stdscr, selected_row_idx)
        elif key == ord('q'):  # Quit
            curses.napms(500)
            break

def edit_screen(stdscr, item_idx):
    curses.curs_set(1)  # Show the cursor

    item = items[item_idx]
    field_idx = 0
    fields = ["col1", "col2", "col3", "col4"]
    editing = False
    input_buffer = ""

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        if h < 10 or w < 40:
            stdscr.addstr(0, 0, "Window size is too small")
            stdscr.refresh()
            continue

        # Draw double-line border around the screen using Unicode characters
        stdscr.addstr(0, 0, "╔" + "═" * (w - 2) + "╗")
        stdscr.addstr(h-2, 0, "╚" + "═" * (w - 2) + "╝")
        for i in range(1, h-2):
            stdscr.addstr(i, 0, "║")
            stdscr.addstr(i, w-1, "║")

        title = "Edit Screen"
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(1, w//2 - len(title)//2, title)
        stdscr.attroff(curses.color_pair(1))

        for idx, field in enumerate(fields):
            y = idx + 3
            if idx == field_idx:
                stdscr.attron(curses.color_pair(2))
                if editing:
                    stdscr.addstr(y, 3, f"{field}: {input_buffer}")
                else:
                    stdscr.addstr(y, 3, f"{field}: {item[field]}")
                stdscr.attroff(curses.color_pair(2))
            else:
                stdscr.addstr(y, 3, f"{field}: {item[field]}")

        draw_prompt(stdscr, "E" if editing else " ")

        key = stdscr.getch()

        if not editing:
            draw_prompt(stdscr, ">", key)
            if key == curses.KEY_UP and field_idx > 0:
                field_idx -= 1
            elif key == curses.KEY_DOWN and field_idx < len(fields) - 1:
                field_idx += 1
            elif key == ord('e'):  # Enter edit mode
                curses.napms(500)
                editing = True
                input_buffer = item[fields[field_idx]]
            elif key == ord('x'):  # Exit edit screen
                curses.napms(500)
                break
        else:
            if key == 27:  # ESC to exit edit mode
                draw_prompt(stdscr, "ESC")
                stdscr.refresh()
                curses.napms(500)
                editing = False
                input_buffer = ""
            elif key == curses.KEY_UP and field_idx > 0:
                field_idx -= 1
                input_buffer = item[fields[field_idx]]
            elif key == curses.KEY_DOWN and field_idx < len(fields) - 1:
                field_idx += 1
                input_buffer = item[fields[field_idx]]
            elif key == 10:  # Enter key to save changes
                item[fields[field_idx]] = input_buffer
                field_idx += 1
                if field_idx >= len(fields):
                    field_idx = len(fields) - 1
                    editing = False
                input_buffer = item[fields[field_idx]]
            elif key == curses.KEY_BACKSPACE or key == 127:
                input_buffer = input_buffer[:-1]
            else:
                input_buffer += chr(key)

        stdscr.refresh()

    curses.curs_set(0)  # Hide the cursor again

# Main function to initialize curses and start the UI
def main(stdscr):
    main_menu(stdscr)

# Run the program
curses.wrapper(main)
