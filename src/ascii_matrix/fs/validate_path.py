from pathlib import Path

VALID_EXTENSIONS = { ".png", ".jpg", ".jpeg", ".gif", ".webp" }

def validate_image_path(path: str) -> Path:
    path_obj = Path(path)

    if not path_obj.exists():
        raise FileNotFoundError(f"Image not found: {path}")

    if not path_obj.is_file():
        raise ValueError(f"Not a file: {path}")

    if path_obj.suffix.lower() not in VALID_EXTENSIONS:
        raise ValueError(f"Unsupported image type: {path_obj.suffix}")

    return path_obj
