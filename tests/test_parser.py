import pytest
from ascii_matrix.cli.parser import parse_args

def test_parse_args_with_no_image_and_color():
    with pytest.raises(SystemExit):
        parse_args([])

def test_parse_args_with_image_and_no_color():
    args = parse_args(["-i", "dog.png"])

    assert args.image == "dog.png"
    assert args.color == "white"

def test_parse_args_with_color_and_no_image():
    with pytest.raises(SystemExit):
        parse_args(["--color", "red"])

def test_parse_args_with_image_and_invalid_color():
    with pytest.raises(SystemExit):
        parse_args(["--image", "cat.png", "--color", "cyan"])

def test_parse_args_with_image_and_color():
    args = parse_args(["-i", "squirrel.png", "-c", "green"])

    assert args.image == "squirrel.png"
    assert args.color == "green"
