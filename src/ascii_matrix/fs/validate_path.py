from pathlib import Path
from ascii_matrix.constants import VALID_EXTENSIONS

def validate_image_path(path: str) -> Path:
    path_obj = Path(path).expanduser().resolve()

    if not path_obj.exists():
        raise FileNotFoundError(f"Image not found: {path}")

    if not path_obj.is_file():
        raise ValueError(f"Not a file: {path}")

    if path_obj.suffix.lower() not in VALID_EXTENSIONS:
        raise ValueError(f"Unsupported image type: {path_obj.suffix}")

    return path_obj
