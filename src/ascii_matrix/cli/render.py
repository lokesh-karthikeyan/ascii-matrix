import os
import time

def render(frames):
    clear = lambda: os.system("cls" if os.name == "nt" else "clear")

    for frame in frames:
        clear()

        print(frame)

        time.sleep(0.05)
