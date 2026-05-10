import pytest
from pathlib import Path
from ascii_matrix.fs.validate_path import validate_image_path

def test_validate_image_path_with_incorrect_path():
    with pytest.raises(FileNotFoundError):
        validate_image_path("not_exist.png")

def test_validate_image_path_with_a_directory(tmp_path):
    dir_path = tmp_path / "images"
    dir_path.mkdir()

    with pytest.raises(ValueError):
        validate_image_path(str(dir_path))

def test_validate_image_path_with_an_invalid_extension(tmp_path):
    text_file_path = tmp_path / "image.txt"
    text_file_path.write_text("I'm an image")

    with pytest.raises(ValueError):
        validate_image_path(str(text_file_path))

def test_validate_image_path_with_a_valid_image(tmp_path):
    penguin_image = tmp_path / "penguin.png"
    penguin_image.write_bytes(b"I'm a penguin")

    result = validate_image_path(str(penguin_image))

    assert isinstance(result, Path)
    assert result.name == "penguin.png"
