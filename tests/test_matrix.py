import pytest
import random
from unittest.mock import patch
from ascii_matrix.effects.matrix import matrix

def test_matrix_rows():
    ascii_text = "ABC\nDEF"
    color      = "red"
    gen        = matrix(ascii_text, color)

    frame = next(gen)
    lines = frame.splitlines()

    assert len(lines) == 2

def test_matrix_generator_yields_different_frames():
    ascii_text = "####"
    color      = "green"

    with patch('random.randint', return_value=0):
        gen = matrix(ascii_text, color)

        frame_1 = next(gen)
        frame_2 = next(gen)

        assert frame_1 != frame_2

def test_matrix_contain_reset_codes():
    ascii_text = "A"
    color      = "blue"
    gen        = matrix(ascii_text, color)

    frame = next(gen)

    assert "\033[0m" in frame
