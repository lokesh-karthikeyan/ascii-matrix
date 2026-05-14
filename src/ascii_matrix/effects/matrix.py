import random
from ascii_matrix.constants import MATRIX_CHARS, RESET, COLOR_MAP, TRAIL

def matrix(ascii_text, color_str):
    color = COLOR_MAP[color_str]
    rows = ascii_text.splitlines()
    height, width = len(rows), len(rows[0])
    drops = [random.randint(-20, 0) for _ in range(width)]

    head_color = COLOR_MAP["white"]

    while True:
        frame = []

        for index, row_str in enumerate(rows):
            current_row = "".join([
                f"{head_color}{random.choice(MATRIX_CHARS)}{RESET}" if index == drop else
                f"{color}{random.choice(MATRIX_CHARS)}{RESET}" if drop - TRAIL < index < drop else
                f"{color}{character}{RESET}"
                for character, drop in zip(row_str, drops)
            ])

            frame.append(current_row)

        yield "\n".join(frame)

        drops = [drop + 1 if drop <= height else random.randint(-20, 0) for drop in drops]
