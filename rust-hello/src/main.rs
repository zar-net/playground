use crossterm::{
    execute,
    style::{Color, Print, SetForegroundColor},
    terminal::{Clear, ClearType},
    cursor::{MoveTo, Hide, Show},
    ExecutableCommand,
};
use std::io::{stdout, Write};

fn main() {
    let mut stdout = stdout();

    // Clear the screen and hide the cursor
    stdout.execute(Clear(ClearType::All)).unwrap();
    stdout.execute(Hide).unwrap();

    // Get terminal size
    let (cols, rows) = crossterm::terminal::size().unwrap();

    // Calculate the position to center the text
    let text = "Hello, World!";
    let x = (cols / 2) - (text.len() as u16 / 2);
    let y = rows / 2;

    // Move cursor to position and print "Hello" in green
    stdout.execute(MoveTo(x, y)).unwrap();
    stdout.execute(SetForegroundColor(Color::Green)).unwrap();
    stdout.execute(Print("Hello")).unwrap();

    // Define bronze color as an RGB value
    let bronze = Color::Rgb { r: 205, g: 127, b: 50 };

    // Print the rest of the text in default color
    stdout.execute(SetForegroundColor(bronze)).unwrap();
    stdout.execute(Print(", Bronze!")).unwrap();

    // Show the cursor and flush the output
    stdout.execute(Show).unwrap();
    stdout.flush().unwrap();

    // Wait for user input before exiting
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
}
