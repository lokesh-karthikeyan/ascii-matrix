from pathlib import Path
from PIL import Image as PILImage
import shutil

class Image:
    def __init__(self, path: str | Path):
        self.path  = path

        terminal_width, _ = shutil.get_terminal_size()

        with PILImage.open(self.path) as img:
            width, height     = img.size
            aspect_ratio      = height / width
            correction_factor = 0.55

            new_height = int(terminal_width * aspect_ratio * correction_factor)
            self.image = img.resize((terminal_width, new_height))
