import time
import shutil

TERMINAL_WIDTH     = shutil.get_terminal_size().columns
STAR_ROW_COUNT     = 5
ROCKET_LABEL_START = 5
ROCKET_LABEL_END   = 11
MOON_RIGHT_MARGIN  = 4

RESET  = "\033[0m"
WHITE  = "\033[97m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
GRAY   = "\033[90m"
DIM    = "\033[2m"
BOLD   = "\033[1m"

STAR_ROWS = [
    "  * . · * + · * . · + * . · * + . · * + . · * . + · * . + · * + . · * . + * ·    ",
    "· + * . · * + · . * · + * . · + * · . * + · * . · + * · . + * · . * + · . * + ·  ",
]

def star_line(row_idx):
    s = STAR_ROWS[row_idx % len(STAR_ROWS)]
    return (s * 3)[:TERMINAL_WIDTH]

def make_trajectory(width, rows=6):
    moon_col  = width - MOON_RIGHT_MARGIN
    start_col = width // 2 + 2
    step = (moon_col - start_col) // rows
    lines = []
    for r in range(rows):
        col = moon_col - step * r
        line = " " * col + "· · ·"
        lines.append(line[:width])
    return lines

def pad_center(text, width):
    return text.center(width)

rocket_raw = [
    "/\\",
    "/  \\",
    "/ /\\ \\",
    "/ /  \\ \\",
    "| |    | |",
    "|A|    | |",
    "|R|    | |",
    "|T|    | |",
    "|E|    | |",
    "|M|    | |",
    "|I|    | |",
    "|S|    | |",
    "|_|    |_|",
    "/   \\  /   \\",
    "/ NASA\\/ NASA\\",
    "|_______|_______|",
    "| |",
    "| |",
]

flames_raw = [
    ")) (( ))",
    "(((  |  )))",
    "\\\\  |  //",
]

def slow_print(text, delay=0.04):
    print(text)
    time.sleep(delay)

def print_scene():
    print()

    for i in range(STAR_ROW_COUNT):
        slow_print(GRAY + DIM + star_line(i) + RESET, 0.06)

    moon_line = " " * (TERMINAL_WIDTH - MOON_RIGHT_MARGIN) + YELLOW + BOLD + "☽" + RESET
    slow_print(moon_line, 0.1)
    print()

    for t in make_trajectory(TERMINAL_WIDTH):
        slow_print(CYAN + DIM + t + RESET, 0.08)

    print()

    for i, line in enumerate(rocket_raw):
        centered = pad_center(line, TERMINAL_WIDTH)
        is_label_row = ROCKET_LABEL_START <= i <= ROCKET_LABEL_END
        if is_label_row:
            slow_print(CYAN + BOLD + centered + RESET, 0.07)
        else:
            slow_print(WHITE + centered + RESET, 0.07)

    for f in flames_raw:
        slow_print(YELLOW + pad_center(f, TERMINAL_WIDTH) + RESET, 0.1)

    print()
    slow_print(GRAY + "━" * TERMINAL_WIDTH + RESET, 0.2)
    print()
    slow_print(CYAN  + BOLD + pad_center("ARTEMIS  II  —  RUMBO  A  LA  LUNA", TERMINAL_WIDTH) + RESET, 0.15)
    slow_print(GRAY         + pad_center("01  ·  ABRIL  ·  2026", TERMINAL_WIDTH) + RESET, 0.12)
    slow_print(WHITE + DIM  + pad_center("Primer vuelo tripulado desde Apollo 17", TERMINAL_WIDTH) + RESET, 0.1)
    print()

print("\033[2J\033[H")
print(GRAY + "$python artemis.py" + RESET)
print()
time.sleep(0.5)
print_scene()
