import shutil
from pathlib import Path
from PIL import Image as PILImage
from ascii_matrix.constants import CORRECTION_FACTOR

class Image:
    def __init__(self, path: str | Path):
        self.path  = path

        terminal_width, terminal_height = shutil.get_terminal_size()

        with PILImage.open(self.path) as img:
            width, height     = img.size
            aspect_ratio      = height / width

            new_width  = terminal_width
            new_height = int(new_width * aspect_ratio * CORRECTION_FACTOR)

            if new_height > terminal_height:
                new_height = terminal_height
                new_width  = int(new_height / (aspect_ratio * CORRECTION_FACTOR))

            self.image = img.resize((new_width, new_height))
