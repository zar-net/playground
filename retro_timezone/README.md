# Retro Time Zone Display

This Python script displays the current date, time, and timezone information for specified timezones in a retro, organized manner using the `curses` library. The script allows for a colorful, text-based user interface that can fit within 80 or 120 columns, based on user input.

## Features

- Displays the current date, time, and timezone information for multiple timezones.
- Retro-style interface using the `curses` library.
- Color options for display (amber or green).
- Adjusts layout to fit within 80 or 120 columns.
- Ensures consistent borders and spacing around boxes.

## Prerequisites

- Python 3.x
- `pytz` library

You can install `pytz` using pip:

```bash
pip install pytz
```

## How to Run

Save the script as retro_timezone_display.py.
Run the script using Python with the desired color and width options.

## Command-line Arguments

--color: Set the display color. Choices are amber or green. Default is amber.
--width: Set the display width. Choices are 80 or 120 columns. Default is 80.

### Example Usage

```bash
python retro_timezone_display.py --color amber --width 80
```

```bash
python retro_timezone_display.py --color green --width 120
```
