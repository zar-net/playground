# Curses UI Examples
These Python script demonstrates a basic curses-based user interface (UI) for navigating and editing items in a list. The UI includes features such as screen navigation, editing modes, and a command prompt.

## Dependencies

- Python 3.x
- The `curses` module (included with Python on Unix-like systems).

## Running the Script

To run the script, use the following command in your terminal:

```bash
python example1.py
```

## Files and Notes

### Example One
![example1_screen](https://github.com/user-attachments/assets/08293780-c6c9-480a-9837-fd4e7509f675)

#### 1. **Screen Navigation**
   - The UI allows users to navigate through a list of items displayed on the main screen.
   - Users can use the arrow keys to move up and down through the list.

#### 2. **Single-Line Border**
   - A single-line border surrounds the main menu screen, providing a clear boundary for the UI elements.

#### 3. **Double-Line Border**
   - A double-line border surrounds the edit screen, visually distinguishing it from the main menu screen.

#### 4. **Command Prompt**
   - A command prompt is displayed at the bottom of the screen. The prompt is centered with two spaces from the left and right screen edges.
   - The prompt shows the last key pressed by the user, providing immediate feedback.
   - The prompt changes when entering edit mode to indicate the current state (`"[E>]"`).

#### 5. **Editing Mode**
   - Users can enter an editing mode by pressing the `e` key on the edit screen.
   - While in editing mode, users can modify the selected field's value.
   - Arrow keys allow users to navigate between different fields.
   - The Enter key saves the current field's value and moves to the next field.
   - The `ESC` key exits editing mode.

#### 6. **Interacting with Items**
   - Users can interact with a selected item by pressing the `i` key on the main menu, which opens the edit screen for that item.
   - The edit screen displays four fields corresponding to the selected item.

#### 7. **Exiting the Edit Screen**
   - The edit screen can be exited by pressing the `x` key, returning the user to the main menu.

#### 8. **Error Handling and Screen Size Check**
   - The UI includes error handling for key presses, ensuring only printable characters are shown in the command prompt.
   - The UI checks the terminal window size to ensure it is large enough to display the interface. If the window is too small, a warning message is displayed.

### Key Bindings

- **Up Arrow**: Move up through the list or fields.
- **Down Arrow**: Move down through the list or fields.
- **Space**: Select an item in the list.
- **i**: Interact with a selected item (open the edit screen).
- **e**: Enter edit mode on the edit screen.
- **ESC**: Exit edit mode.
- **Enter**: Save the current field's value and move to the next field.
- **x**: Exit the edit screen.
- **q**: Quit the application.
