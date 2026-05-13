import random

MATRIX_CHARS = "マミムメモガギグゲゴ108965QWERTYUIOPASDFGHJKLZXCVBnmwqpdbkloivcxz+=-:. "
WHITE        = "\033[97m"
RESET        = "\033[0m"
COLOR_MAP = {
    "green": "\033[92m",
    "red":   "\033[91m",
    "blue":  "\033[94m",
    "white": "\033[97m",
}

def matrix(ascii_text, color_str):
    color = COLOR_MAP[color_str]
    rows = ascii_text.splitlines()
    height, width = len(rows), len(rows[0])
    trail = 8
    drops = [random.randint(-20, 0) for _ in range(width)]

    while True:
        frame = []

        for index, row_str in enumerate(rows):
            current_row = "".join([
                f"{WHITE}{random.choice(MATRIX_CHARS)}{RESET}" if index == drop else
                f"{color}{random.choice(MATRIX_CHARS)}{RESET}" if drop - trail < index < drop else
                f"{color}{character}{RESET}"
                for character, drop in zip(row_str, drops)
            ])

            frame.append(current_row)

        yield "\n".join(frame)

        drops = [drop + 1 if drop <= height else random.randint(-20, 0) for drop in drops]
