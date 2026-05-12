import pytest
from PIL import Image as PILImage
from ascii_matrix.ascii_image.to_ascii import to_ascii

def test_to_ascii():
    width, height = 20, 10
    image = PILImage.new("L", (width, height), color=128)

    result = to_ascii(image)
    lines  = result.strip().split("\n")

    assert isinstance(result, str)
    assert len(lines[0]) == width
    assert len(lines) == height
