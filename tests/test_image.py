import pytest
from pathlib import Path
from PIL import Image as PILImage
from ascii_matrix.ascii_image.image import Image

@pytest.fixture
def sample_image(tmp_path):
    path = tmp_path / "sample.png"
    img  = PILImage.new("RGB", (200, 100), color="red")

    img.save(path)

    return path

def test_image_resizes(sample_image, monkeypatch):
    monkeypatch.setattr(
        "shutil.get_terminal_size",
        lambda: (100, 40),
    )

    img = Image(sample_image)

    width, height = img.image.size

    expected_height = int(100 * (100 / 200) * 0.55)
    assert width == 100
    assert height == expected_height

def test_image_is_pil_image(sample_image):
    img = Image(sample_image)

    assert isinstance(img.image, PILImage.Image)

def test_image_invalid():
    with pytest.raises(FileNotFoundError):
        Image("does_not_exist.png")
